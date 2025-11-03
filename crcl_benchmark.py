#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║           CRCL BENCHMARK & PERFORMANCE ANALYZER                              ║
║                                                                              ║
║  Teljesítmény mérés és összehasonlítás különböző konfigurációkkal           ║
║  Performance measurement and comparison with different configurations        ║
║                                                                              ║
║  Author: Czink Ákos József                                                   ║
║  SECUND AI Research Initiative                                               ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import time
import statistics
import json
import csv
from datetime import datetime
from typing import Dict, List, Any, Tuple
from crcl_engine import CRCLEngine, Metrics
from crcl_visualizer import CRCLVisualizer


class CRCLBenchmark:
    """
    CRCL Performance Benchmark Suite
    """
    
    def __init__(self):
        self.visualizer = CRCLVisualizer()
        self.results = []
        
    def benchmark_single_cycle(self, iterations: int = 10) -> Dict[str, Any]:
        """
        Egyetlen ciklus performance mérése
        Measure performance of single cycle
        """
        print(f"\n{self.visualizer.colorize('⏱️  Single Cycle Benchmark', 'bold')}")
        print(f"Iterations: {iterations}")
        
        times = []
        metrics_list = []
        
        problem = {
            'type': 'benchmark',
            'description': 'Performance measurement',
            'complexity': 'medium'
        }
        
        for i in range(iterations):
            engine = CRCLEngine()
            
            start_time = time.time()
            result = engine.execute_full_cycle(problem)
            end_time = time.time()
            
            elapsed = end_time - start_time
            times.append(elapsed)
            metrics_list.append(result['final_metrics'])
            
            print(f"  Iteration {i+1}/{iterations}: {elapsed:.4f}s", end='\r')
        
        print()  # New line after progress
        
        return {
            'test': 'single_cycle',
            'iterations': iterations,
            'times': times,
            'avg_time': statistics.mean(times),
            'min_time': min(times),
            'max_time': max(times),
            'std_dev': statistics.stdev(times) if len(times) > 1 else 0,
            'metrics': metrics_list
        }
    
    def benchmark_convergence(self, cycles_list: List[int] = [1, 3, 5]) -> Dict[str, Any]:
        """
        Konvergencia teljesítmény mérése különböző ciklus számokkal
        Measure convergence performance with different cycle counts
        """
        print(f"\n{self.visualizer.colorize('📈 Convergence Benchmark', 'bold')}")
        
        results = []
        
        problem = {
            'type': 'convergence_benchmark',
            'description': 'Multi-cycle performance test',
            'target_rbb': 9.2
        }
        
        for cycles in cycles_list:
            print(f"\nTesting with {cycles} cycles...")
            engine = CRCLEngine()
            
            start_time = time.time()
            result = engine.converge(problem, max_cycles=cycles)
            end_time = time.time()
            
            elapsed = end_time - start_time
            
            results.append({
                'cycles': cycles,
                'time': elapsed,
                'converged': result['converged'],
                'final_rbb': result['final_metrics'].rbb if result['final_metrics'] else 0,
                'loops_executed': len(result['history'])
            })
            
            print(f"  Time: {elapsed:.4f}s | Converged: {result['converged']}")
        
        return {
            'test': 'convergence',
            'results': results
        }
    
    def benchmark_metrics_calculation(self, iterations: int = 1000) -> Dict[str, Any]:
        """
        Metrika számítási sebesség mérése
        Measure metrics calculation speed
        """
        print(f"\n{self.visualizer.colorize('🧮 Metrics Calculation Benchmark', 'bold')}")
        print(f"Iterations: {iterations}")
        
        from crcl_engine import MetricsCalculator
        calc = MetricsCalculator()
        
        benchmarks = {}
        
        # RBB benchmark
        start = time.time()
        for _ in range(iterations):
            calc.compute_rbb(9.0, 9.0)
        benchmarks['rbb'] = (time.time() - start) / iterations
        
        # CPA benchmark
        start = time.time()
        for _ in range(iterations):
            calc.compute_cpa(8.5, 8.5, 8.5)
        benchmarks['cpa'] = (time.time() - start) / iterations
        
        # CGAS benchmark
        start = time.time()
        for _ in range(iterations):
            calc.compute_cgas(9.0, 9.0)
        benchmarks['cgas'] = (time.time() - start) / iterations
        
        # CMD benchmark
        start = time.time()
        for _ in range(iterations):
            calc.compute_cmd(8.0, 8.0, 8.0)
        benchmarks['cmd'] = (time.time() - start) / iterations
        
        # SR benchmark
        start = time.time()
        for _ in range(iterations):
            calc.compute_sr(9.0, 0.1)
        benchmarks['sr'] = (time.time() - start) / iterations
        
        # tofu benchmark
        start = time.time()
        for _ in range(iterations):
            calc.compute_tofu(0, 100)
        benchmarks['tofu'] = (time.time() - start) / iterations
        
        for metric, time_val in benchmarks.items():
            print(f"  {metric.upper()}: {time_val*1000:.6f}ms per calculation")
        
        return {
            'test': 'metrics_calculation',
            'iterations': iterations,
            'times': benchmarks,
            'total_time': sum(benchmarks.values())
        }
    
    def benchmark_loop_classes(self) -> Dict[str, Any]:
        """
        Különböző loop osztályok teljesítményének mérése
        Measure performance of different loop classes
        """
        print(f"\n{self.visualizer.colorize('🔄 Loop Classes Benchmark', 'bold')}")
        
        engine = CRCLEngine()
        results = {}
        
        problem = {'type': 'loop_test', 'data': 'sample'}
        
        # Perception Loop
        start = time.time()
        state = engine.run_perception_loop(problem)
        results['perception'] = time.time() - start
        print(f"  Perception (A): {results['perception']:.6f}s")
        
        # Evaluation Loop
        start = time.time()
        state = engine.run_evaluation_loop({'response': 'test'})
        results['evaluation'] = time.time() - start
        print(f"  Evaluation (B): {results['evaluation']:.6f}s")
        
        # Correction Loop
        start = time.time()
        state = engine.run_correction_loop(['issue1', 'issue2'])
        results['correction'] = time.time() - start
        print(f"  Correction (C): {results['correction']:.6f}s")
        
        # Meta-Cognitive Loop
        start = time.time()
        state = engine.run_meta_cognitive_loop()
        results['meta_cognitive'] = time.time() - start
        print(f"  Meta-Cognitive (D): {results['meta_cognitive']:.6f}s")
        
        return {
            'test': 'loop_classes',
            'times': results,
            'total_time': sum(results.values())
        }
    
    def run_full_benchmark_suite(self) -> Dict[str, Any]:
        """
        Teljes benchmark csomag futtatása
        Run complete benchmark suite
        """
        print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                   🏃 CRCL FULL BENCHMARK SUITE 🏃                            ║
║                                                                              ║
║                     Performance Analysis & Metrics                           ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
        """)
        
        suite_start = time.time()
        
        results = {
            'timestamp': datetime.now().isoformat(),
            'benchmarks': {}
        }
        
        # 1. Single Cycle
        results['benchmarks']['single_cycle'] = self.benchmark_single_cycle(iterations=10)
        
        # 2. Convergence
        results['benchmarks']['convergence'] = self.benchmark_convergence([1, 3, 5])
        
        # 3. Metrics Calculation
        results['benchmarks']['metrics'] = self.benchmark_metrics_calculation(iterations=1000)
        
        # 4. Loop Classes
        results['benchmarks']['loops'] = self.benchmark_loop_classes()
        
        suite_end = time.time()
        results['total_duration'] = suite_end - suite_start
        
        return results
    
    def generate_report(self, results: Dict[str, Any]) -> str:
        """
        Részletes jelentés generálása
        Generate detailed report
        """
        report = []
        
        report.append("\n" + "="*80)
        report.append(self.visualizer.colorize("📊 CRCL BENCHMARK REPORT", 'bold'))
        report.append("="*80)
        
        report.append(f"\nTimestamp: {results['timestamp']}")
        report.append(f"Total Duration: {results['total_duration']:.2f}s")
        
        # Single Cycle Results
        if 'single_cycle' in results['benchmarks']:
            sc = results['benchmarks']['single_cycle']
            report.append(f"\n{self.visualizer.colorize('1️⃣  SINGLE CYCLE PERFORMANCE', 'bold')}")
            report.append(f"   Iterations: {sc['iterations']}")
            report.append(f"   Average Time: {sc['avg_time']*1000:.2f}ms")
            report.append(f"   Min Time: {sc['min_time']*1000:.2f}ms")
            report.append(f"   Max Time: {sc['max_time']*1000:.2f}ms")
            report.append(f"   Std Dev: {sc['std_dev']*1000:.2f}ms")
            
            if sc['metrics']:
                avg_rbb = statistics.mean([m.rbb for m in sc['metrics']])
                avg_tofu = statistics.mean([m.tofu for m in sc['metrics']])
                report.append(f"   Average RBB: {avg_rbb:.3f}")
                report.append(f"   Average tofu: {avg_tofu:.3f} {'✓' if avg_tofu == 0 else '✗'}")
        
        # Convergence Results
        if 'convergence' in results['benchmarks']:
            conv = results['benchmarks']['convergence']
            report.append(f"\n{self.visualizer.colorize('2️⃣  CONVERGENCE PERFORMANCE', 'bold')}")
            
            for r in conv['results']:
                report.append(f"   {r['cycles']} cycles: {r['time']:.4f}s | "
                            f"RBB: {r['final_rbb']:.3f} | "
                            f"Loops: {r['loops_executed']}")
        
        # Metrics Calculation Results
        if 'metrics' in results['benchmarks']:
            metrics = results['benchmarks']['metrics']
            report.append(f"\n{self.visualizer.colorize('3️⃣  METRICS CALCULATION SPEED', 'bold')}")
            
            for metric, time_val in metrics['times'].items():
                report.append(f"   {metric.upper()}: {time_val*1000000:.2f}μs per call")
            
            total_ops = metrics['iterations'] * len(metrics['times'])
            report.append(f"   Total Operations: {total_ops:,}")
            report.append(f"   Operations/sec: {total_ops/metrics['total_time']:,.0f}")
        
        # Loop Classes Results
        if 'loops' in results['benchmarks']:
            loops = results['benchmarks']['loops']
            report.append(f"\n{self.visualizer.colorize('4️⃣  LOOP CLASSES PERFORMANCE', 'bold')}")
            
            for loop_name, time_val in loops['times'].items():
                report.append(f"   {loop_name.capitalize()}: {time_val*1000:.2f}ms")
            
            report.append(f"   Total: {loops['total_time']*1000:.2f}ms")
        
        # Performance Summary
        report.append(f"\n{self.visualizer.colorize('📈 PERFORMANCE SUMMARY', 'bold')}")
        
        if 'single_cycle' in results['benchmarks']:
            sc = results['benchmarks']['single_cycle']
            throughput = 1.0 / sc['avg_time']
            report.append(f"   Throughput: {throughput:.2f} cycles/second")
        
        if 'metrics' in results['benchmarks']:
            metrics = results['benchmarks']['metrics']
            total_ops = metrics['iterations'] * len(metrics['times'])
            ops_per_sec = total_ops / metrics['total_time']
            report.append(f"   Metrics Ops/sec: {ops_per_sec:,.0f}")
        
        report.append("\n" + "="*80)
        report.append(self.visualizer.colorize("✅ BENCHMARK COMPLETED", 'green'))
        report.append("="*80 + "\n")
        
        return "\n".join(report)
    
    def export_results(self, results: Dict[str, Any], prefix: str = "benchmark"):
        """
        Eredmények exportálása JSON és CSV formátumban
        Export results in JSON and CSV format
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # JSON Export
        json_file = f"{prefix}_{timestamp}.json"
        with open(json_file, 'w') as f:
            json.dump(results, f, indent=2, default=str)
        
        print(f"\n✅ JSON export: {self.visualizer.colorize(json_file, 'green')}")
        
        # CSV Export (simplified)
        csv_file = f"{prefix}_{timestamp}.csv"
        with open(csv_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Test', 'Metric', 'Value', 'Unit'])
            
            # Single cycle data
            if 'single_cycle' in results['benchmarks']:
                sc = results['benchmarks']['single_cycle']
                writer.writerow(['single_cycle', 'avg_time', sc['avg_time'], 'seconds'])
                writer.writerow(['single_cycle', 'min_time', sc['min_time'], 'seconds'])
                writer.writerow(['single_cycle', 'max_time', sc['max_time'], 'seconds'])
            
            # Convergence data
            if 'convergence' in results['benchmarks']:
                for r in results['benchmarks']['convergence']['results']:
                    writer.writerow(['convergence', f"{r['cycles']}_cycles", r['time'], 'seconds'])
            
            # Metrics calculation data
            if 'metrics' in results['benchmarks']:
                for metric, time_val in results['benchmarks']['metrics']['times'].items():
                    writer.writerow(['metrics_calc', metric, time_val, 'seconds'])
        
        print(f"✅ CSV export: {self.visualizer.colorize(csv_file, 'green')}")


def main():
    """Main benchmark execution"""
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                🔬 CRCL PERFORMANCE BENCHMARK SYSTEM 🔬                       ║
║                                                                              ║
║                     Comprehensive Performance Analysis                       ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)
    
    benchmark = CRCLBenchmark()
    
    print("\nStarting benchmark suite...")
    print("This will take approximately 30-60 seconds.\n")
    
    # Run benchmark suite
    results = benchmark.run_full_benchmark_suite()
    
    # Generate and print report
    report = benchmark.generate_report(results)
    print(report)
    
    # Export results
    benchmark.export_results(results, prefix="crcl_benchmark")
    
    print("\n✨ Benchmark completed successfully!")
    print("Check the generated JSON and CSV files for detailed results.\n")


if __name__ == "__main__":
    main()
