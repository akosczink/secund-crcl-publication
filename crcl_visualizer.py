#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║               CRCL VISUALIZER - Interactive Analysis Tool                    ║
║                                                                              ║
║  Interaktív vizualizáció a CRCL metrikák és fejlődés követésére             ║
║  Interactive visualization for CRCL metrics and development tracking         ║
║                                                                              ║
║  Author: Czink Ákos József                                                   ║
║  SECUND AI Research Initiative                                               ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import json
import time
from typing import List, Dict, Any
from crcl_engine import CRCLEngine, Metrics, LoopState


class CRCLVisualizer:
    """
    CRCL Vizualizátor - Metrikák és fejlődés vizuális megjelenítése
    CRCL Visualizer - Visual display of metrics and development
    """
    
    def __init__(self):
        self.colors = {
            'green': '\033[92m',
            'yellow': '\033[93m',
            'red': '\033[91m',
            'blue': '\033[94m',
            'cyan': '\033[96m',
            'magenta': '\033[95m',
            'bold': '\033[1m',
            'reset': '\033[0m'
        }
    
    def colorize(self, text: str, color: str) -> str:
        """Színes szöveg generálása"""
        return f"{self.colors.get(color, '')}{text}{self.colors['reset']}"
    
    def draw_bar(self, value: float, max_value: float = 10.0, 
                 width: int = 40, threshold: float = 9.0) -> str:
        """
        Progress bar rajzolása
        Draw progress bar
        """
        percentage = min(value / max_value, 1.0)
        filled = int(percentage * width)
        empty = width - filled
        
        # Színezés a threshold alapján
        if value >= threshold:
            color = 'green'
        elif value >= threshold * 0.85:
            color = 'yellow'
        else:
            color = 'red'
        
        bar = '█' * filled + '░' * empty
        return self.colorize(bar, color)
    
    def display_metrics(self, metrics: Metrics, title: str = "Metrics") -> None:
        """
        Metrikák vizuális megjelenítése
        Visual display of metrics
        """
        print(f"\n{self.colorize('═' * 80, 'cyan')}")
        print(self.colorize(f"  {title}", 'bold'))
        print(self.colorize('═' * 80, 'cyan'))
        
        metrics_info = [
            ('RBB', metrics.rbb, 9.2, 'Reality-Believability Balance'),
            ('CPA', metrics.cpa, 8.5, 'Central Processing Axis'),
            ('CGAS', metrics.cgas, 8.0, 'Cognitive Grounding & Stability'),
            ('CMD', metrics.cmd, 7.5, 'Cognitive Meta Depth'),
            ('SR', metrics.sr, 0.85, 'Stability Ratio (0-1)'),
            ('tofu', metrics.tofu, 0.0, 'Truth-Over-Fiction Unit'),
        ]
        
        for name, value, target, description in metrics_info:
            # Speciális kezelés az SR és tofu számára
            if name == 'SR':
                max_val = 1.0
            elif name == 'tofu':
                max_val = 1.0
                target = 0.0
            else:
                max_val = 10.0
            
            bar = self.draw_bar(value if name != 'tofu' else 1.0 - value, 
                              max_val, threshold=target)
            
            status = '✓' if (value >= target if name != 'tofu' else value == target) else '⚠'
            status_color = 'green' if status == '✓' else 'yellow'
            
            print(f"  {self.colorize(name.ljust(6), 'bold')}: "
                  f"{bar} "
                  f"{self.colorize(f'{value:.3f}', 'cyan')} / {target:.3f} "
                  f"{self.colorize(status, status_color)}")
            print(f"         {self.colorize(description, 'blue')}")
        
        # Összesített státusz
        is_optimal = metrics.is_optimal()
        overall_status = "OPTIMAL ✓" if is_optimal else "IN PROGRESS..."
        overall_color = 'green' if is_optimal else 'yellow'
        
        print(f"\n  {self.colorize('Overall Status:', 'bold')} "
              f"{self.colorize(overall_status, overall_color)}")
        print(self.colorize('═' * 80, 'cyan'))
    
    def display_loop_history(self, history: List[LoopState]) -> None:
        """
        Hurok történet vizualizálása
        Visualize loop history
        """
        print(f"\n{self.colorize('🔄 LOOP HISTORY', 'bold')}")
        print(self.colorize('─' * 80, 'cyan'))
        
        for i, state in enumerate(history):
            loop_class = state.loop_class.value
            loop_names = {
                'A': 'PERCEPTION',
                'B': 'EVALUATION', 
                'C': 'CORRECTION',
                'D': 'META-COGNITIVE'
            }
            
            print(f"\n  {self.colorize(f'#{i+1}', 'yellow')} "
                  f"Loop Class {self.colorize(loop_class, 'magenta')} - "
                  f"{self.colorize(loop_names.get(loop_class, 'UNKNOWN'), 'bold')}")
            print(f"     Iteration: {state.iteration}")
            print(f"     RBB: {self.colorize(f'{state.metrics.rbb:.3f}', 'cyan')} | "
                  f"CPA: {self.colorize(f'{state.metrics.cpa:.3f}', 'cyan')} | "
                  f"CGAS: {self.colorize(f'{state.metrics.cgas:.3f}', 'cyan')} | "
                  f"tofu: {self.colorize(f'{state.metrics.tofu:.3f}', 'green' if state.metrics.tofu == 0 else 'red')}")
            
            if state.improvements:
                print(f"     Improvements: {self.colorize(', '.join(state.improvements[:2]), 'green')}")
        
        print(self.colorize('─' * 80, 'cyan'))
    
    def display_convergence_graph(self, history: List[LoopState], 
                                  metric_name: str = 'rbb') -> None:
        """
        Konvergencia grafikon ASCII művészettel
        Convergence graph with ASCII art
        """
        print(f"\n{self.colorize(f'📈 CONVERGENCE GRAPH - {metric_name.upper()}', 'bold')}")
        print(self.colorize('─' * 80, 'cyan'))
        
        if not history:
            print("  No data available")
            return
        
        # Értékek kinyerése
        values = [getattr(state.metrics, metric_name) for state in history]
        
        # Normalizálás 0-20 magasságra
        max_val = max(values) if values else 10.0
        min_val = min(values) if values else 0.0
        height = 15
        
        # Grafikon rajzolása
        for h in range(height, -1, -1):
            line = f"  {(min_val + (max_val - min_val) * h / height):5.2f} │"
            
            for val in values:
                normalized = int((val - min_val) / (max_val - min_val) * height)
                if normalized >= h:
                    line += self.colorize('▓▓', 'green')
                else:
                    line += '  '
            
            print(line)
        
        # X tengely
        print(f"       └{'──' * len(values)}")
        print(f"         " + "".join([self.colorize(f'{i+1}'.center(2), 'yellow') 
                                      for i in range(len(values))]))
        print(f"         {self.colorize('Iterations', 'bold')}")
        
        # Statisztikák
        if len(values) > 1:
            improvement = values[-1] - values[0]
            print(f"\n  Initial: {self.colorize(f'{values[0]:.3f}', 'cyan')} → "
                  f"Final: {self.colorize(f'{values[-1]:.3f}', 'cyan')} "
                  f"(Δ: {self.colorize(f'{improvement:+.3f}', 'green' if improvement > 0 else 'red')})")
        
        print(self.colorize('─' * 80, 'cyan'))
    
    def display_comparison_table(self, history: List[LoopState]) -> None:
        """
        Összehasonlító táblázat az iterációk között
        Comparison table between iterations
        """
        if len(history) < 2:
            return
        
        print(f"\n{self.colorize('📊 METRICS COMPARISON TABLE', 'bold')}")
        print(self.colorize('═' * 80, 'cyan'))
        
        # Fejléc
        print(f"  {'Metric':<8} │ {'First':<8} │ {'Last':<8} │ {'Change':<10} │ {'%':<8}")
        print(self.colorize('  ' + '─' * 70, 'cyan'))
        
        first = history[0].metrics
        last = history[-1].metrics
        
        metrics_to_compare = [
            ('RBB', first.rbb, last.rbb),
            ('CPA', first.cpa, last.cpa),
            ('CGAS', first.cgas, last.cgas),
            ('CMD', first.cmd, last.cmd),
            ('SR', first.sr, last.sr),
            ('tofu', first.tofu, last.tofu),
        ]
        
        for name, first_val, last_val in metrics_to_compare:
            change = last_val - first_val
            pct = (change / first_val * 100) if first_val != 0 else 0
            
            change_str = f"{change:+.3f}"
            pct_str = f"{pct:+.1f}%"
            
            change_color = 'green' if change > 0 else ('red' if change < 0 else 'yellow')
            if name == 'tofu':
                change_color = 'green' if change <= 0 else 'red'
            
            print(f"  {name:<8} │ {first_val:8.3f} │ {last_val:8.3f} │ "
                  f"{self.colorize(change_str, change_color):<19} │ "
                  f"{self.colorize(pct_str, change_color):<16}")
        
        print(self.colorize('═' * 80, 'cyan'))
    
    def animate_convergence(self, engine: CRCLEngine, problem: Dict[str, Any],
                          max_cycles: int = 5, delay: float = 1.0) -> None:
        """
        Animált konvergencia folyamat
        Animated convergence process
        """
        print(f"\n{self.colorize('🎬 ANIMATED CONVERGENCE VISUALIZATION', 'bold')}")
        print(self.colorize('═' * 80, 'cyan'))
        
        for cycle in range(max_cycles):
            print(f"\n{self.colorize(f'CYCLE {cycle + 1}/{max_cycles}', 'yellow')}")
            
            result = engine.execute_full_cycle(problem)
            
            # Aktuális metrikák megjelenítése
            self.display_metrics(result['meta_cognitive'], 
                               f"Cycle {cycle + 1} Results")
            
            if result['optimal']:
                print(f"\n{self.colorize('🎉 CONVERGENCE ACHIEVED!', 'green')}")
                break
            
            time.sleep(delay)
        
        # Végső összefoglalás
        self.display_loop_history(engine.loop_history)
        self.display_convergence_graph(engine.loop_history, 'rbb')
        self.display_comparison_table(engine.loop_history)


def demo_basic_visualization():
    """Alapvető vizualizációs demo"""
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                    🎨 CRCL VISUALIZER DEMONSTRATION 🎨                       ║
║                                                                              ║
║              Interactive Visualization of CRCL Metrics                       ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)
    
    visualizer = CRCLVisualizer()
    
    # Példa metrikák
    print(visualizer.colorize("\n1️⃣  INITIAL STATE (Sub-optimal)", 'bold'))
    initial_metrics = Metrics(
        rbb=7.8, cpa=7.2, cgas=7.5, cmd=6.8, sr=0.72, tofu=0.0, lsi=0.65
    )
    visualizer.display_metrics(initial_metrics, "Initial State")
    
    time.sleep(1)
    
    print(visualizer.colorize("\n2️⃣  AFTER OPTIMIZATION", 'bold'))
    optimized_metrics = Metrics(
        rbb=9.4, cpa=8.9, cgas=9.1, cmd=8.5, sr=0.91, tofu=0.0, lsi=0.92
    )
    visualizer.display_metrics(optimized_metrics, "Optimized State")


def demo_full_visualization():
    """Teljes vizualizációs demo motorral"""
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                  🚀 FULL CRCL ENGINE + VISUALIZER DEMO 🚀                    ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)
    
    visualizer = CRCLVisualizer()
    engine = CRCLEngine()
    
    problem = {
        'type': 'cognitive_optimization',
        'description': 'Achieve maximum RBB with zero hallucination',
        'constraints': ['tofu = 0', 'RBB >= 9.2', 'all metrics optimal'],
        'domain': 'SECUND OS'
    }
    
    print(visualizer.colorize("\n🎯 Problem Definition:", 'bold'))
    print(json.dumps(problem, indent=2))
    
    # Animált konvergencia
    visualizer.animate_convergence(engine, problem, max_cycles=3, delay=0.5)
    
    # Végső jelentés
    print(engine.generate_report())
    
    print(f"\n{visualizer.colorize('✨ Visualization completed successfully!', 'green')}")


if __name__ == "__main__":
    import sys
    
    mode = sys.argv[1] if len(sys.argv) > 1 else 'full'
    
    if mode == 'basic':
        demo_basic_visualization()
    else:
        demo_full_visualization()
