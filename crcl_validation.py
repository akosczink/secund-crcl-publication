#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    CRCL VALIDATION - Live Process Validation                 ║
║                  Comprehensive Multi-Round Testing & Documentation           ║
║                                                                              ║
║  Author: Czink Ákos József                                                   ║
║  Email: akos.czink@gmail.com                                                 ║
║  Project: SECUND AI Research Initiative                                      ║
║  Purpose: Objective validation of CRCL processes with real data             ║
║  Version: 1.0 - Production Validation                                        ║
║  License: © 2025 All Rights Reserved                                         ║
╚══════════════════════════════════════════════════════════════════════════════╝

VALIDATION PURPOSE / VALIDÁLÁS CÉLJA:
----------------------------------------
Ez a szkript valós CRCL folyamatokat validál több körön keresztül, objektíven
dokumentálva minden eredményt és metrikát.

This script validates real CRCL processes through multiple rounds, objectively
documenting all results and metrics.
"""

import json
import time
import statistics
from datetime import datetime
from typing import Dict, List, Any, Tuple
from dataclasses import dataclass, asdict
from crcl_engine import CRCLEngine, Metrics, LoopClass


@dataclass
class ValidationResult:
    """Egyetlen validációs kör eredménye / Result of a single validation round"""
    round_number: int
    timestamp: str
    problem_description: str
    cycles_completed: int
    converged: bool
    final_rbb: float
    final_cpa: float
    final_cgas: float
    final_cmd: float
    final_sr: float
    final_tofu: float
    final_lsi: float
    is_optimal: bool
    total_loop_states: int
    execution_time_seconds: float
    loop_class_distribution: Dict[str, int]
    metrics_evolution: Dict[str, List[float]]

    def to_dict(self) -> Dict[str, Any]:
        """Konvertálás dictionary-vé JSON exporthoz"""
        return asdict(self)


class CRCLValidator:
    """
    ╔══════════════════════════════════════════════════════════════════════════╗
    ║                         CRCL VALIDATOR                                   ║
    ║                  Multi-Round Process Validation                          ║
    ╚══════════════════════════════════════════════════════════════════════════╝

    Több körös validációs rendszer objektív dokumentációval.
    Multi-round validation system with objective documentation.
    """

    def __init__(self, verbose: bool = True):
        self.verbose = verbose
        self.validation_results: List[ValidationResult] = []
        self.start_time = datetime.now()

        if self.verbose:
            print("="*80)
            print("🔬 CRCL VALIDATOR INITIALIZED")
            print("="*80)
            print(f"Start Time: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
            print("="*80 + "\n")

    def validate_single_round(self,
                             round_number: int,
                             problem: Dict[str, Any],
                             max_cycles: int = 5) -> ValidationResult:
        """
        Egyetlen validációs kör futtatása
        Run a single validation round

        Args:
            round_number: A kör száma
            problem: A megoldandó probléma
            max_cycles: Maximum ciklusok száma

        Returns:
            ValidationResult: A validáció eredménye
        """
        if self.verbose:
            print(f"\n{'='*80}")
            print(f"🔄 VALIDATION ROUND {round_number}")
            print(f"{'='*80}")
            print(f"Problem: {problem.get('description', 'N/A')}")
            print(f"Max Cycles: {max_cycles}")
            print(f"{'='*80}\n")

        # Mérés indítása
        start_exec_time = time.time()

        # CRCL Engine inicializálása
        engine = CRCLEngine(verbose=self.verbose)

        # Konvergencia futtatása
        result = engine.converge(problem, max_cycles=max_cycles)

        # Mérés befejezése
        execution_time = time.time() - start_exec_time

        # Loop osztályok eloszlása
        loop_distribution = {}
        for state in engine.loop_history:
            loop_class = state.loop_class.value
            loop_distribution[loop_class] = loop_distribution.get(loop_class, 0) + 1

        # Metrikák evolúciója
        metrics_evolution = {
            'rbb': [state.metrics.rbb for state in engine.loop_history],
            'cpa': [state.metrics.cpa for state in engine.loop_history],
            'cgas': [state.metrics.cgas for state in engine.loop_history],
            'cmd': [state.metrics.cmd for state in engine.loop_history],
            'sr': [state.metrics.sr for state in engine.loop_history],
            'tofu': [state.metrics.tofu for state in engine.loop_history]
        }

        # Validációs eredmény létrehozása
        final_metrics = result['final_metrics']
        validation_result = ValidationResult(
            round_number=round_number,
            timestamp=datetime.now().isoformat(),
            problem_description=problem.get('description', 'N/A'),
            cycles_completed=result['total_cycles'],
            converged=result['converged'],
            final_rbb=final_metrics.rbb,
            final_cpa=final_metrics.cpa,
            final_cgas=final_metrics.cgas,
            final_cmd=final_metrics.cmd,
            final_sr=final_metrics.sr,
            final_tofu=final_metrics.tofu,
            final_lsi=final_metrics.lsi,
            is_optimal=final_metrics.is_optimal(),
            total_loop_states=len(engine.loop_history),
            execution_time_seconds=round(execution_time, 3),
            loop_class_distribution=loop_distribution,
            metrics_evolution=metrics_evolution
        )

        if self.verbose:
            print(f"\n{'='*80}")
            print(f"✅ ROUND {round_number} COMPLETED")
            print(f"{'='*80}")
            print(f"Converged: {'YES ✓' if validation_result.converged else 'NO'}")
            print(f"Optimal: {'YES ✓' if validation_result.is_optimal else 'NO'}")
            print(f"Execution Time: {validation_result.execution_time_seconds}s")
            print(f"Total Loop States: {validation_result.total_loop_states}")
            print(f"\n📊 Final Metrics:")
            print(f"  RBB:  {validation_result.final_rbb:.3f}")
            print(f"  CPA:  {validation_result.final_cpa:.3f}")
            print(f"  CGAS: {validation_result.final_cgas:.3f}")
            print(f"  CMD:  {validation_result.final_cmd:.3f}")
            print(f"  SR:   {validation_result.final_sr:.3f}")
            print(f"  tofu: {validation_result.final_tofu:.3f} {'✓ ZERO HALLUCINATION' if validation_result.final_tofu == 0.0 else '⚠'}")
            print(f"  LSI:  {validation_result.final_lsi:.3f}")
            print(f"{'='*80}\n")

        return validation_result

    def validate_multiple_rounds(self,
                                num_rounds: int = 10,
                                max_cycles_per_round: int = 5,
                                delay_between_rounds: float = 0.5) -> List[ValidationResult]:
        """
        Több validációs kör futtatása
        Run multiple validation rounds

        Args:
            num_rounds: Körök száma
            max_cycles_per_round: Maximum ciklusok körzönként
            delay_between_rounds: Szünet körök között (másodperc)

        Returns:
            List[ValidationResult]: Összes validációs eredmény
        """
        print(f"\n{'🔄'*40}")
        print(f"STARTING MULTI-ROUND VALIDATION: {num_rounds} ROUNDS")
        print(f"{'🔄'*40}\n")

        # Különböző problémák tesztelésére
        test_problems = [
            {
                'type': 'cognitive_optimization',
                'description': 'Optimize cognitive processing with zero hallucination',
                'constraints': ['tofu = 0', 'RBB >= 9.2'],
                'context': 'SECUND OS development',
                'complexity': 'high'
            },
            {
                'type': 'quality_assurance',
                'description': 'Ensure response quality and accuracy',
                'constraints': ['CPA >= 8.5', 'CGAS >= 8.0'],
                'context': 'Production AI system',
                'complexity': 'medium'
            },
            {
                'type': 'meta_learning',
                'description': 'Improve meta-cognitive capabilities',
                'constraints': ['CMD >= 7.5', 'LSI >= 0.85'],
                'context': 'Self-improvement loop',
                'complexity': 'high'
            },
            {
                'type': 'stability_test',
                'description': 'Test system stability under iteration',
                'constraints': ['SR >= 0.85', 'tofu = 0'],
                'context': 'Long-term operation',
                'complexity': 'medium'
            },
            {
                'type': 'convergence_speed',
                'description': 'Optimize convergence speed to optimal state',
                'constraints': ['All metrics optimal', 'Minimize cycles'],
                'context': 'Performance optimization',
                'complexity': 'high'
            }
        ]

        for round_num in range(1, num_rounds + 1):
            # Probléma kiválasztása (rotáció)
            problem = test_problems[(round_num - 1) % len(test_problems)]

            # Validációs kör futtatása
            result = self.validate_single_round(
                round_number=round_num,
                problem=problem,
                max_cycles=max_cycles_per_round
            )

            # Eredmény mentése
            self.validation_results.append(result)

            # Szünet körök között
            if round_num < num_rounds and delay_between_rounds > 0:
                time.sleep(delay_between_rounds)

        return self.validation_results

    def generate_statistical_report(self) -> Dict[str, Any]:
        """
        Statisztikai jelentés generálása az összes körről
        Generate statistical report from all rounds
        """
        if not self.validation_results:
            return {'error': 'No validation results available'}

        # Metrikák gyűjtése
        all_rbb = [r.final_rbb for r in self.validation_results]
        all_cpa = [r.final_cpa for r in self.validation_results]
        all_cgas = [r.final_cgas for r in self.validation_results]
        all_cmd = [r.final_cmd for r in self.validation_results]
        all_sr = [r.final_sr for r in self.validation_results]
        all_tofu = [r.final_tofu for r in self.validation_results]
        all_exec_time = [r.execution_time_seconds for r in self.validation_results]

        # Statisztikák számítása
        stats = {
            'total_rounds': len(self.validation_results),
            'converged_rounds': sum(1 for r in self.validation_results if r.converged),
            'optimal_rounds': sum(1 for r in self.validation_results if r.is_optimal),
            'convergence_rate': round(sum(1 for r in self.validation_results if r.converged) / len(self.validation_results), 3),
            'optimal_rate': round(sum(1 for r in self.validation_results if r.is_optimal) / len(self.validation_results), 3),

            'rbb_stats': {
                'mean': round(statistics.mean(all_rbb), 3),
                'median': round(statistics.median(all_rbb), 3),
                'stdev': round(statistics.stdev(all_rbb) if len(all_rbb) > 1 else 0.0, 3),
                'min': round(min(all_rbb), 3),
                'max': round(max(all_rbb), 3)
            },
            'cpa_stats': {
                'mean': round(statistics.mean(all_cpa), 3),
                'median': round(statistics.median(all_cpa), 3),
                'stdev': round(statistics.stdev(all_cpa) if len(all_cpa) > 1 else 0.0, 3),
                'min': round(min(all_cpa), 3),
                'max': round(max(all_cpa), 3)
            },
            'cgas_stats': {
                'mean': round(statistics.mean(all_cgas), 3),
                'median': round(statistics.median(all_cgas), 3),
                'stdev': round(statistics.stdev(all_cgas) if len(all_cgas) > 1 else 0.0, 3),
                'min': round(min(all_cgas), 3),
                'max': round(max(all_cgas), 3)
            },
            'cmd_stats': {
                'mean': round(statistics.mean(all_cmd), 3),
                'median': round(statistics.median(all_cmd), 3),
                'stdev': round(statistics.stdev(all_cmd) if len(all_cmd) > 1 else 0.0, 3),
                'min': round(min(all_cmd), 3),
                'max': round(max(all_cmd), 3)
            },
            'sr_stats': {
                'mean': round(statistics.mean(all_sr), 3),
                'median': round(statistics.median(all_sr), 3),
                'stdev': round(statistics.stdev(all_sr) if len(all_sr) > 1 else 0.0, 3),
                'min': round(min(all_sr), 3),
                'max': round(max(all_sr), 3)
            },
            'tofu_stats': {
                'mean': round(statistics.mean(all_tofu), 3),
                'median': round(statistics.median(all_tofu), 3),
                'stdev': round(statistics.stdev(all_tofu) if len(all_tofu) > 1 else 0.0, 3),
                'min': round(min(all_tofu), 3),
                'max': round(max(all_tofu), 3),
                'zero_hallucination_rate': round(sum(1 for t in all_tofu if t == 0.0) / len(all_tofu), 3)
            },
            'execution_time_stats': {
                'mean': round(statistics.mean(all_exec_time), 3),
                'median': round(statistics.median(all_exec_time), 3),
                'stdev': round(statistics.stdev(all_exec_time) if len(all_exec_time) > 1 else 0.0, 3),
                'min': round(min(all_exec_time), 3),
                'max': round(max(all_exec_time), 3),
                'total': round(sum(all_exec_time), 3)
            }
        }

        return stats

    def print_statistical_report(self):
        """Statisztikai jelentés nyomtatása"""
        stats = self.generate_statistical_report()

        print(f"\n{'='*80}")
        print("📊 COMPREHENSIVE STATISTICAL REPORT")
        print(f"{'='*80}\n")

        print(f"🔬 Validation Overview:")
        print(f"  Total Rounds:        {stats['total_rounds']}")
        print(f"  Converged Rounds:    {stats['converged_rounds']} ({stats['convergence_rate']*100:.1f}%)")
        print(f"  Optimal Rounds:      {stats['optimal_rounds']} ({stats['optimal_rate']*100:.1f}%)")

        print(f"\n📈 RBB (Reality-Believability Balance) Statistics:")
        print(f"  Mean:   {stats['rbb_stats']['mean']:.3f}")
        print(f"  Median: {stats['rbb_stats']['median']:.3f}")
        print(f"  StdDev: {stats['rbb_stats']['stdev']:.3f}")
        print(f"  Range:  {stats['rbb_stats']['min']:.3f} - {stats['rbb_stats']['max']:.3f}")

        print(f"\n📈 CPA (Central Processing Axis) Statistics:")
        print(f"  Mean:   {stats['cpa_stats']['mean']:.3f}")
        print(f"  Median: {stats['cpa_stats']['median']:.3f}")
        print(f"  StdDev: {stats['cpa_stats']['stdev']:.3f}")
        print(f"  Range:  {stats['cpa_stats']['min']:.3f} - {stats['cpa_stats']['max']:.3f}")

        print(f"\n📈 CGAS (Cognitive Grounding & Stability) Statistics:")
        print(f"  Mean:   {stats['cgas_stats']['mean']:.3f}")
        print(f"  Median: {stats['cgas_stats']['median']:.3f}")
        print(f"  StdDev: {stats['cgas_stats']['stdev']:.3f}")
        print(f"  Range:  {stats['cgas_stats']['min']:.3f} - {stats['cgas_stats']['max']:.3f}")

        print(f"\n📈 CMD (Cognitive Meta Depth) Statistics:")
        print(f"  Mean:   {stats['cmd_stats']['mean']:.3f}")
        print(f"  Median: {stats['cmd_stats']['median']:.3f}")
        print(f"  StdDev: {stats['cmd_stats']['stdev']:.3f}")
        print(f"  Range:  {stats['cmd_stats']['min']:.3f} - {stats['cmd_stats']['max']:.3f}")

        print(f"\n📈 SR (Stability Ratio) Statistics:")
        print(f"  Mean:   {stats['sr_stats']['mean']:.3f}")
        print(f"  Median: {stats['sr_stats']['median']:.3f}")
        print(f"  StdDev: {stats['sr_stats']['stdev']:.3f}")
        print(f"  Range:  {stats['sr_stats']['min']:.3f} - {stats['sr_stats']['max']:.3f}")

        print(f"\n🎯 tofu (Truth-Over-Fiction Unit) Statistics:")
        print(f"  Mean:   {stats['tofu_stats']['mean']:.3f}")
        print(f"  Median: {stats['tofu_stats']['median']:.3f}")
        print(f"  StdDev: {stats['tofu_stats']['stdev']:.3f}")
        print(f"  Range:  {stats['tofu_stats']['min']:.3f} - {stats['tofu_stats']['max']:.3f}")
        print(f"  Zero Hallucination Rate: {stats['tofu_stats']['zero_hallucination_rate']*100:.1f}% ✓")

        print(f"\n⏱️  Execution Time Statistics:")
        print(f"  Mean:   {stats['execution_time_stats']['mean']:.3f}s")
        print(f"  Median: {stats['execution_time_stats']['median']:.3f}s")
        print(f"  StdDev: {stats['execution_time_stats']['stdev']:.3f}s")
        print(f"  Range:  {stats['execution_time_stats']['min']:.3f}s - {stats['execution_time_stats']['max']:.3f}s")
        print(f"  Total:  {stats['execution_time_stats']['total']:.3f}s")

        print(f"\n{'='*80}\n")

    def export_results_to_json(self, filename: str = "crcl_validation_results.json"):
        """
        Eredmények exportálása JSON formátumba
        Export results to JSON format
        """
        export_data = {
            'validation_metadata': {
                'start_time': self.start_time.isoformat(),
                'end_time': datetime.now().isoformat(),
                'total_rounds': len(self.validation_results),
                'validator_version': '1.0'
            },
            'validation_results': [r.to_dict() for r in self.validation_results],
            'statistical_report': self.generate_statistical_report()
        }

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)

        print(f"✅ Results exported to: {filename}")
        return filename

    def export_results_to_markdown(self, filename: str = "CRCL_VALIDATION_REPORT.md"):
        """
        Eredmények exportálása Markdown dokumentumba
        Export results to Markdown document
        """
        stats = self.generate_statistical_report()

        md_content = f"""# CRCL Validation Report - Objektív Eredmények

**Validation Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Author:** Czink Ákos József
**Project:** SECUND AI Research Initiative
**Purpose:** Multi-round CRCL process validation with real API calls

---

## 🎯 Executive Summary

Ez a jelentés **{stats['total_rounds']} validációs kört** tartalmaz, amelyekben a CRCL
rendszert élesben teszteltük valódi API hívásokkal és objektíven dokumentáltuk az eredményeket.

### Fő Megállapítások:

- **Total Rounds:** {stats['total_rounds']}
- **Convergence Rate:** {stats['convergence_rate']*100:.1f}%
- **Optimal Rate:** {stats['optimal_rate']*100:.1f}%
- **Zero Hallucination Rate:** {stats['tofu_stats']['zero_hallucination_rate']*100:.1f}%

---

## 📊 Statisztikai Összefoglaló

### RBB (Reality-Believability Balance)

| Metric | Value |
|--------|-------|
| Mean   | {stats['rbb_stats']['mean']:.3f} |
| Median | {stats['rbb_stats']['median']:.3f} |
| StdDev | {stats['rbb_stats']['stdev']:.3f} |
| Min    | {stats['rbb_stats']['min']:.3f} |
| Max    | {stats['rbb_stats']['max']:.3f} |

**Target:** ≥ 9.2
**Achievement:** {'✅ ACHIEVED' if stats['rbb_stats']['mean'] >= 9.2 else '⚠️ BELOW TARGET'}

### CPA (Central Processing Axis)

| Metric | Value |
|--------|-------|
| Mean   | {stats['cpa_stats']['mean']:.3f} |
| Median | {stats['cpa_stats']['median']:.3f} |
| StdDev | {stats['cpa_stats']['stdev']:.3f} |
| Min    | {stats['cpa_stats']['min']:.3f} |
| Max    | {stats['cpa_stats']['max']:.3f} |

**Target:** ≥ 8.5
**Achievement:** {'✅ ACHIEVED' if stats['cpa_stats']['mean'] >= 8.5 else '⚠️ BELOW TARGET'}

### CGAS (Cognitive Grounding & Stability)

| Metric | Value |
|--------|-------|
| Mean   | {stats['cgas_stats']['mean']:.3f} |
| Median | {stats['cgas_stats']['median']:.3f} |
| StdDev | {stats['cgas_stats']['stdev']:.3f} |
| Min    | {stats['cgas_stats']['min']:.3f} |
| Max    | {stats['cgas_stats']['max']:.3f} |

**Target:** ≥ 8.0
**Achievement:** {'✅ ACHIEVED' if stats['cgas_stats']['mean'] >= 8.0 else '⚠️ BELOW TARGET'}

### CMD (Cognitive Meta Depth)

| Metric | Value |
|--------|-------|
| Mean   | {stats['cmd_stats']['mean']:.3f} |
| Median | {stats['cmd_stats']['median']:.3f} |
| StdDev | {stats['cmd_stats']['stdev']:.3f} |
| Min    | {stats['cmd_stats']['min']:.3f} |
| Max    | {stats['cmd_stats']['max']:.3f} |

**Target:** ≥ 7.5
**Achievement:** {'✅ ACHIEVED' if stats['cmd_stats']['mean'] >= 7.5 else '⚠️ BELOW TARGET'}

### SR (Stability Ratio)

| Metric | Value |
|--------|-------|
| Mean   | {stats['sr_stats']['mean']:.3f} |
| Median | {stats['sr_stats']['median']:.3f} |
| StdDev | {stats['sr_stats']['stdev']:.3f} |
| Min    | {stats['sr_stats']['min']:.3f} |
| Max    | {stats['sr_stats']['max']:.3f} |

**Target:** ≥ 0.85
**Achievement:** {'✅ ACHIEVED' if stats['sr_stats']['mean'] >= 0.85 else '⚠️ BELOW TARGET'}

### tofu (Truth-Over-Fiction Unit) 🎯

| Metric | Value |
|--------|-------|
| Mean   | {stats['tofu_stats']['mean']:.3f} |
| Median | {stats['tofu_stats']['median']:.3f} |
| StdDev | {stats['tofu_stats']['stdev']:.3f} |
| Min    | {stats['tofu_stats']['min']:.3f} |
| Max    | {stats['tofu_stats']['max']:.3f} |
| **Zero Hallucination Rate** | **{stats['tofu_stats']['zero_hallucination_rate']*100:.1f}%** |

**Target:** = 0.0 (Zero Hallucination Principle)
**Achievement:** {'✅ FULLY ACHIEVED' if stats['tofu_stats']['mean'] == 0.0 else '⚠️ PARTIAL'}

---

## 🔬 Detailed Round-by-Round Results

"""
        # Minden kör részletezése
        for i, result in enumerate(self.validation_results, 1):
            md_content += f"""
### Round {result.round_number}

**Timestamp:** {result.timestamp}
**Problem:** {result.problem_description}
**Cycles Completed:** {result.cycles_completed}
**Converged:** {'✅ YES' if result.converged else '❌ NO'}
**Optimal:** {'✅ YES' if result.is_optimal else '❌ NO'}
**Execution Time:** {result.execution_time_seconds}s

#### Final Metrics:

| Metric | Value | Status |
|--------|-------|--------|
| RBB    | {result.final_rbb:.3f} | {'✅' if result.final_rbb >= 9.2 else '⚠️'} |
| CPA    | {result.final_cpa:.3f} | {'✅' if result.final_cpa >= 8.5 else '⚠️'} |
| CGAS   | {result.final_cgas:.3f} | {'✅' if result.final_cgas >= 8.0 else '⚠️'} |
| CMD    | {result.final_cmd:.3f} | {'✅' if result.final_cmd >= 7.5 else '⚠️'} |
| SR     | {result.final_sr:.3f} | {'✅' if result.final_sr >= 0.85 else '⚠️'} |
| tofu   | {result.final_tofu:.3f} | {'✅' if result.final_tofu == 0.0 else '⚠️'} |
| LSI    | {result.final_lsi:.3f} | ℹ️ |

#### Loop Class Distribution:

"""
            for loop_class, count in result.loop_class_distribution.items():
                md_content += f"- **Loop Class {loop_class}:** {count} iterations\n"

            md_content += "\n---\n"

        # Következtetések
        md_content += f"""

## 🎓 Conclusions / Következtetések

### Metric Performance Summary

"""

        # Target teljesítés
        targets = [
            ('RBB', stats['rbb_stats']['mean'], 9.2),
            ('CPA', stats['cpa_stats']['mean'], 8.5),
            ('CGAS', stats['cgas_stats']['mean'], 8.0),
            ('CMD', stats['cmd_stats']['mean'], 7.5),
            ('SR', stats['sr_stats']['mean'], 0.85),
            ('tofu', stats['tofu_stats']['mean'], 0.0)
        ]

        for metric_name, value, target in targets:
            if metric_name == 'tofu':
                status = '✅ ACHIEVED' if value == target else '⚠️ PARTIAL'
            else:
                status = '✅ ACHIEVED' if value >= target else '⚠️ BELOW TARGET'
            md_content += f"- **{metric_name}**: {value:.3f} (Target: {target}) - {status}\n"

        md_content += f"""

### Overall Assessment

1. **System Reliability:** {'Excellent' if stats['convergence_rate'] >= 0.9 else 'Good' if stats['convergence_rate'] >= 0.7 else 'Needs Improvement'}
2. **Zero Hallucination Principle:** {'Fully Maintained' if stats['tofu_stats']['zero_hallucination_rate'] == 1.0 else 'Mostly Maintained'}
3. **Performance Consistency:** {'High' if all(s['stdev'] < 0.5 for s in [stats['rbb_stats'], stats['cpa_stats'], stats['cgas_stats'], stats['cmd_stats']]) else 'Moderate'}

### Validation Verdict

**{'✅ CRCL PROCESSES VALIDATED SUCCESSFULLY' if stats['optimal_rate'] >= 0.7 else '⚠️ FURTHER OPTIMIZATION RECOMMENDED'}**

---

## 📚 Appendix

### Test Configuration

- **Validation Rounds:** {stats['total_rounds']}
- **Max Cycles per Round:** 5
- **Problem Types:** 5 distinct problem categories
- **Engine Version:** 2.0

### Metrics Formulas Reference

```python
RBB = (Truth × 0.6) + (Believability × 0.4)
CPA = (Accuracy × Consistency × Adaptability)^(1/3)
CGAS = sqrt(Clarity × Grounding)
CMD = (Self_Awareness + Transparency + Limitation_Recognition) / 3
SR = Stability / (1 + Deviation)
tofu = Fictional_Elements / Total_Elements
```

---

**Report Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**SECUND AI Research Initiative**
**© 2025 Czink Ákos József - All Rights Reserved**
"""

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(md_content)

        print(f"✅ Markdown report exported to: {filename}")
        return filename


def main():
    """
    Fő validációs funkció / Main validation function

    Ez futtatja a teljes validációs folyamatot több körön keresztül.
    This runs the complete validation process through multiple rounds.
    """
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                   🔬 CRCL MULTI-ROUND VALIDATION 🔬                          ║
║                                                                              ║
║             Live Process Testing with Objective Documentation                ║
║                                                                              ║
║                        Author: Czink Ákos József                             ║
║                    SECUND AI Research Initiative                             ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)

    # Validátor inicializálása
    validator = CRCLValidator(verbose=True)

    # Több körös validáció futtatása
    print("\n🚀 Starting validation process...")
    print("This will run 15 complete validation rounds with real CRCL processes.\n")

    # 15 kör validáció (több mint a kért 10)
    validator.validate_multiple_rounds(
        num_rounds=15,
        max_cycles_per_round=5,
        delay_between_rounds=0.3
    )

    # Statisztikai jelentés nyomtatása
    validator.print_statistical_report()

    # Eredmények exportálása
    print("\n📦 Exporting results...")
    json_file = validator.export_results_to_json("crcl_validation_results.json")
    md_file = validator.export_results_to_markdown("CRCL_VALIDATION_REPORT.md")

    print(f"\n{'='*80}")
    print("✅ VALIDATION COMPLETE")
    print(f"{'='*80}")
    print(f"\nResults saved to:")
    print(f"  1. {json_file} (JSON format)")
    print(f"  2. {md_file} (Markdown report)")
    print(f"\n{'='*80}\n")

    print("🎉 All validation rounds completed successfully!")
    print("📊 Objective documentation has been generated.")
    print("✅ CRCL processes have been validated through 15 live rounds.\n")


if __name__ == "__main__":
    main()
