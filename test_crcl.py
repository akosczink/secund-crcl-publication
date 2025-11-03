#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    CRCL TEST SUITE - Comprehensive Testing                   ║
║                                                                              ║
║  Teljes tesztelési keretrendszer a CRCL engine validálására                 ║
║  Complete testing framework for CRCL engine validation                       ║
║                                                                              ║
║  Author: Czink Ákos József                                                   ║
║  SECUND AI Research Initiative                                               ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import unittest
import sys
from crcl_engine import (
    MetricsCalculator, CRCLEngine, Metrics, LoopClass,
    QuantumLayer, MetaLayer, RealLayer
)


class TestMetricsCalculator(unittest.TestCase):
    """
    MetricsCalculator osztály tesztjei
    Tests for MetricsCalculator class
    """
    
    def setUp(self):
        self.calc = MetricsCalculator()
    
    def test_compute_rbb_valid(self):
        """RBB számítás érvényes bemenetekkel"""
        result = self.calc.compute_rbb(9.0, 9.0)
        expected = 9.0
        self.assertEqual(result, expected)
        
        result = self.calc.compute_rbb(10.0, 8.0)
        expected = 9.2  # (10 * 0.6) + (8 * 0.4) = 6 + 3.2 = 9.2
        self.assertEqual(result, expected)
    
    def test_compute_rbb_invalid_range(self):
        """RBB számítás érvénytelen tartománnyal"""
        with self.assertRaises(ValueError):
            self.calc.compute_rbb(11.0, 9.0)  # truth > 10
        
        with self.assertRaises(ValueError):
            self.calc.compute_rbb(9.0, -1.0)  # believability < 0
    
    def test_compute_cpa_valid(self):
        """CPA számítás érvényes bemenetekkel"""
        result = self.calc.compute_cpa(8.0, 8.0, 8.0)
        expected = 8.0
        self.assertEqual(result, expected)
        
        # Geometrikus átlag teszt
        result = self.calc.compute_cpa(9.0, 8.0, 7.0)
        expected = round((9.0 * 8.0 * 7.0) ** (1/3), 3)
        self.assertEqual(result, expected)
    
    def test_compute_cgas_valid(self):
        """CGAS számítás érvényes bemenetekkel"""
        result = self.calc.compute_cgas(9.0, 9.0)
        expected = 9.0
        self.assertEqual(result, expected)
        
        result = self.calc.compute_cgas(8.0, 8.0)
        expected = 8.0
        self.assertEqual(result, expected)
    
    def test_compute_cmd_valid(self):
        """CMD számítás érvényes bemenetekkel"""
        result = self.calc.compute_cmd(8.0, 8.0, 8.0)
        expected = 8.0
        self.assertEqual(result, expected)
        
        result = self.calc.compute_cmd(9.0, 8.0, 7.0)
        expected = 8.0
        self.assertEqual(result, expected)
    
    def test_compute_sr_valid(self):
        """SR számítás érvényes bemenetekkel"""
        result = self.calc.compute_sr(9.0, 0.0)
        expected = 9.0
        self.assertEqual(result, expected)
        
        result = self.calc.compute_sr(9.0, 0.1)
        expected = round(9.0 / 1.1, 3)
        self.assertEqual(result, expected)
    
    def test_compute_tofu_zero_hallucination(self):
        """tofu számítás zéró hallucinációval (cél állapot)"""
        result = self.calc.compute_tofu(0, 100)
        expected = 0.0
        self.assertEqual(result, expected)
    
    def test_compute_tofu_with_hallucinations(self):
        """tofu számítás hallucinációkkal"""
        result = self.calc.compute_tofu(5, 100)
        expected = 0.05
        self.assertEqual(result, expected)
    
    def test_compute_tofu_invalid(self):
        """tofu számítás érvénytelen bemenetekkel"""
        with self.assertRaises(ValueError):
            self.calc.compute_tofu(10, 5)  # fictional > total
        
        with self.assertRaises(ValueError):
            self.calc.compute_tofu(-1, 10)  # negative count
    
    def test_compute_lsi_single_value(self):
        """LSI számítás egy értékkel"""
        result = self.calc.compute_lsi([8.5])
        self.assertGreater(result, 0.0)
        self.assertLessEqual(result, 1.0)
    
    def test_compute_lsi_multiple_values(self):
        """LSI számítás több értékkel"""
        values = [8.0, 8.2, 8.5, 8.7, 9.0]
        result = self.calc.compute_lsi(values)
        self.assertGreater(result, 0.0)
        self.assertLessEqual(result, 1.0)
    
    def test_compute_cg_delta_improvement(self):
        """CGΔ számítás javulással"""
        current = Metrics(rbb=9.0, cpa=8.5, cgas=8.5, cmd=8.0)
        previous = Metrics(rbb=8.0, cpa=7.5, cgas=7.5, cmd=7.0)
        
        result = self.calc.compute_cg_delta(current, previous)
        self.assertGreater(result, 0.0)
    
    def test_compute_cg_delta_decline(self):
        """CGΔ számítás visszaeséssel"""
        current = Metrics(rbb=7.0, cpa=6.5, cgas=6.5, cmd=6.0)
        previous = Metrics(rbb=8.0, cpa=7.5, cgas=7.5, cmd=7.0)
        
        result = self.calc.compute_cg_delta(current, previous)
        self.assertLess(result, 0.0)


class TestMetrics(unittest.TestCase):
    """
    Metrics osztály tesztjei
    Tests for Metrics class
    """
    
    def test_metrics_creation(self):
        """Metrics objektum létrehozása"""
        metrics = Metrics(rbb=9.2, cpa=8.5, cgas=8.0, cmd=7.5, sr=0.85, tofu=0.0)
        
        self.assertEqual(metrics.rbb, 9.2)
        self.assertEqual(metrics.cpa, 8.5)
        self.assertEqual(metrics.tofu, 0.0)
    
    def test_metrics_is_optimal_true(self):
        """Optimális metrikák ellenőrzése"""
        metrics = Metrics(
            rbb=9.5, cpa=9.0, cgas=8.5, cmd=8.0, sr=0.90, tofu=0.0
        )
        
        self.assertTrue(metrics.is_optimal())
    
    def test_metrics_is_optimal_false(self):
        """Nem optimális metrikák ellenőrzése"""
        metrics = Metrics(
            rbb=8.0, cpa=7.5, cgas=7.0, cmd=6.5, sr=0.70, tofu=0.0
        )
        
        self.assertFalse(metrics.is_optimal())
    
    def test_metrics_str_representation(self):
        """Metrics string reprezentációja"""
        metrics = Metrics(rbb=9.2, cpa=8.5, cgas=8.0, cmd=7.5, sr=0.85, tofu=0.0)
        
        result = str(metrics)
        self.assertIn('RBB', result)
        self.assertIn('9.200', result)
        self.assertIn('✓', result)


class TestQuantumLayer(unittest.TestCase):
    """
    QuantumLayer osztály tesztjei
    Tests for QuantumLayer class
    """
    
    def setUp(self):
        self.quantum = QuantumLayer()
    
    def test_explore_possibilities(self):
        """Lehetőségek feltárása"""
        problem = {'type': 'test', 'complexity': 'medium'}
        possibilities = self.quantum.explore_possibilities(problem)
        
        self.assertIsInstance(possibilities, list)
        self.assertGreater(len(possibilities), 0)
        self.assertEqual(len(possibilities), self.quantum.exploration_depth)
    
    def test_collapse_superposition(self):
        """Kvantum állapot kollapszálása"""
        problem = {'type': 'test'}
        self.quantum.explore_possibilities(problem)
        
        result = self.quantum.collapse_superposition({'score_weight': 1.0})
        
        self.assertIsInstance(result, dict)
        self.assertIn('path_id', result)
        self.assertIn('potential_score', result)


class TestMetaLayer(unittest.TestCase):
    """
    MetaLayer osztály tesztjei
    Tests for MetaLayer class
    """
    
    def setUp(self):
        self.meta = MetaLayer()
    
    def test_reflect_on_process(self):
        """Folyamatok elemzése"""
        process_log = [
            {'step': 1, 'action': 'perceive'},
            {'step': 2, 'action': 'evaluate'},
            {'step': 3, 'action': 'correct'}
        ]
        
        insights = self.meta.reflect_on_process(process_log)
        
        self.assertIsInstance(insights, dict)
        self.assertIn('patterns', insights)
        self.assertIn('bottlenecks', insights)
        self.assertIn('optimizations', insights)
    
    def test_build_meta_knowledge(self):
        """Meta-tudás építése"""
        initial_level = len(self.meta.meta_knowledge)
        
        self.meta.build_meta_knowledge({'experience': 'test'})
        
        self.assertEqual(len(self.meta.meta_knowledge), initial_level + 1)


class TestRealLayer(unittest.TestCase):
    """
    RealLayer osztály tesztjei
    Tests for RealLayer class
    """
    
    def setUp(self):
        self.real = RealLayer()
    
    def test_execute(self):
        """Döntés végrehajtása"""
        decision = {'path_id': 0, 'potential_score': 8.5}
        
        result, metrics = self.real.execute(decision)
        
        self.assertIsInstance(result, dict)
        self.assertIsInstance(metrics, Metrics)
        self.assertIn('decision_id', result)
        self.assertIn('outcome', result)
        self.assertEqual(result['outcome'], 'success')


class TestCRCLEngine(unittest.TestCase):
    """
    CRCLEngine osztály tesztjei
    Tests for CRCLEngine class
    """
    
    def setUp(self):
        self.engine = CRCLEngine()
    
    def test_engine_initialization(self):
        """Engine inicializálása"""
        self.assertIsNotNone(self.engine.calculator)
        self.assertIsNotNone(self.engine.quantum)
        self.assertIsNotNone(self.engine.meta)
        self.assertIsNotNone(self.engine.real)
        self.assertEqual(self.engine.current_iteration, 0)
    
    def test_run_perception_loop(self):
        """Percepciós hurok futtatása"""
        input_data = {'type': 'test', 'content': 'sample'}
        
        state = self.engine.run_perception_loop(input_data)
        
        self.assertEqual(state.loop_class, LoopClass.PERCEPTION)
        self.assertIsInstance(state.metrics, Metrics)
        self.assertEqual(state.metrics.tofu, 0.0)
    
    def test_run_evaluation_loop(self):
        """Értékelő hurok futtatása"""
        response = {'output': 'test response'}
        
        state = self.engine.run_evaluation_loop(response)
        
        self.assertEqual(state.loop_class, LoopClass.EVALUATION)
        self.assertIsInstance(state.metrics, Metrics)
    
    def test_run_correction_loop(self):
        """Korrektív hurok futtatása"""
        issues = ['Issue 1', 'Issue 2']
        
        state = self.engine.run_correction_loop(issues)
        
        self.assertEqual(state.loop_class, LoopClass.CORRECTION)
        self.assertIsInstance(state.metrics, Metrics)
        self.assertGreater(len(state.improvements), 0)
    
    def test_run_meta_cognitive_loop(self):
        """Meta-kognitív hurok futtatása"""
        # Először futtassunk néhány előzőhurkot
        self.engine.run_perception_loop({'test': 'data'})
        self.engine.run_evaluation_loop({'test': 'response'})
        
        state = self.engine.run_meta_cognitive_loop()
        
        self.assertEqual(state.loop_class, LoopClass.META_COGNITIVE)
        self.assertIsInstance(state.metrics, Metrics)
    
    def test_execute_full_cycle(self):
        """Teljes ciklus végrehajtása"""
        problem = {
            'type': 'test',
            'description': 'Test problem'
        }
        
        result = self.engine.execute_full_cycle(problem)
        
        self.assertIsInstance(result, dict)
        self.assertIn('iteration', result)
        self.assertIn('final_metrics', result)
        self.assertIn('optimal', result)
        self.assertIsInstance(result['optimal'], bool)
    
    def test_converge(self):
        """Konvergencia folyamat"""
        problem = {
            'type': 'optimization',
            'description': 'Test optimization problem'
        }
        
        result = self.engine.converge(problem, max_cycles=2)
        
        self.assertIsInstance(result, dict)
        self.assertIn('total_cycles', result)
        self.assertIn('converged', result)
        self.assertIn('results', result)
        self.assertGreater(len(result['results']), 0)
    
    def test_loop_history_tracking(self):
        """Hurok történet követése"""
        initial_count = len(self.engine.loop_history)
        
        problem = {'type': 'test'}
        self.engine.execute_full_cycle(problem)
        
        # 4 loop class fut minden ciklusban (A, B, C, D)
        self.assertGreater(len(self.engine.loop_history), initial_count)
    
    def test_generate_report(self):
        """Jelentés generálása"""
        problem = {'type': 'test'}
        self.engine.execute_full_cycle(problem)
        
        report = self.engine.generate_report()
        
        self.assertIsInstance(report, str)
        self.assertIn('CRCL ENGINE', report)
        self.assertIn('Total Iterations', report)


class TestIntegration(unittest.TestCase):
    """
    Integrációs tesztek
    Integration tests
    """
    
    def test_full_workflow(self):
        """Teljes munkafolyamat teszt"""
        engine = CRCLEngine()
        
        problem = {
            'type': 'cognitive_optimization',
            'description': 'Optimize with zero hallucination',
            'constraints': ['tofu = 0', 'RBB >= 9.2']
        }
        
        # Konvergálás
        result = engine.converge(problem, max_cycles=2)
        
        # Ellenőrzések
        self.assertGreater(result['total_cycles'], 0)
        self.assertIsNotNone(result['final_metrics'])
        self.assertEqual(result['final_metrics'].tofu, 0.0)
        
        # Jelentés generálása
        report = engine.generate_report()
        self.assertIsInstance(report, str)
    
    def test_metrics_improvement_over_cycles(self):
        """Metrikák javulása ciklusokon keresztül"""
        engine = CRCLEngine()
        
        problem = {'type': 'test'}
        
        # Első ciklus
        result1 = engine.execute_full_cycle(problem)
        
        # További ciklus
        result2 = engine.execute_full_cycle(problem)
        
        # A metrikáknak ugyanolyan jóknak vagy jobbaknak kell lenniük
        # (mivel már az első iterációban optimálisak)
        self.assertGreaterEqual(
            result2['final_metrics'].rbb,
            result1['final_metrics'].rbb - 0.5  # Kis tolerancia
        )


def run_test_suite():
    """
    Teljes tesztelési csomag futtatása
    Run complete test suite
    """
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                    🧪 CRCL TEST SUITE EXECUTION 🧪                           ║
║                                                                              ║
║               Comprehensive Testing Framework for CRCL Engine                ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)
    
    # Test suite létrehozása
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Tesztek hozzáadása
    suite.addTests(loader.loadTestsFromTestCase(TestMetricsCalculator))
    suite.addTests(loader.loadTestsFromTestCase(TestMetrics))
    suite.addTests(loader.loadTestsFromTestCase(TestQuantumLayer))
    suite.addTests(loader.loadTestsFromTestCase(TestMetaLayer))
    suite.addTests(loader.loadTestsFromTestCase(TestRealLayer))
    suite.addTests(loader.loadTestsFromTestCase(TestCRCLEngine))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegration))
    
    # Futtatás
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Összegzés
    print("\n" + "="*80)
    print("📊 TEST SUMMARY")
    print("="*80)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.wasSuccessful():
        print("\n✅ ALL TESTS PASSED!")
    else:
        print("\n❌ SOME TESTS FAILED")
    
    print("="*80)
    
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(run_test_suite())
