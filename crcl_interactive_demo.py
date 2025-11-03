#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║              CRCL INTERACTIVE DEMO - Hands-on Experience                     ║
║                                                                              ║
║  Interaktív bemutató a CRCL rendszer élő kipróbálásához                     ║
║  Interactive demo for hands-on CRCL system experience                       ║
║                                                                              ║
║  Author: Czink Ákos József                                                   ║
║  SECUND AI Research Initiative                                               ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import json
import csv
import time
import sys
from datetime import datetime
from typing import Dict, List, Any, Optional
from crcl_engine import CRCLEngine, Metrics, MetricsCalculator
from crcl_visualizer import CRCLVisualizer


class CRCLInteractiveDemo:
    """
    Interaktív CRCL Demo Rendszer
    Interactive CRCL Demo System
    """
    
    def __init__(self):
        self.engine = CRCLEngine()
        self.visualizer = CRCLVisualizer()
        self.calc = MetricsCalculator()
        self.session_data = []
        self.colors = self.visualizer.colors
    
    def print_header(self, title: str, width: int = 80):
        """Fejléc nyomtatása"""
        print(f"\n{self.visualizer.colorize('═' * width, 'cyan')}")
        print(self.visualizer.colorize(f"  {title.center(width-4)}", 'bold'))
        print(self.visualizer.colorize('═' * width, 'cyan')})
    
    def print_menu(self, title: str, options: List[str]):
        """Menü megjelenítése"""
        print(f"\n{self.visualizer.colorize(title, 'bold')}")
        print(self.visualizer.colorize('─' * 60, 'cyan'))
        for i, option in enumerate(options, 1):
            print(f"  {self.visualizer.colorize(f'{i}.', 'yellow')} {option}")
        print(self.visualizer.colorize('─' * 60, 'cyan'))
    
    def demo_basic_metrics(self):
        """Alapvető metrika számítások bemutatása"""
        self.print_header("🧮 METRIKA SZÁMÍTÁSOK DEMO")
        
        print("\n" + self.visualizer.colorize("1. RBB (Reality-Believability Balance) Számítás", 'bold'))
        print("   Formula: RBB = (Truth × 0.6) + (Believability × 0.4)")
        
        truth = 9.0
        believability = 9.5
        rbb = self.calc.compute_rbb(truth, believability)
        
        print(f"   Truth: {self.visualizer.colorize(f'{truth}', 'cyan')}")
        print(f"   Believability: {self.visualizer.colorize(f'{believability}', 'cyan')}")
        print(f"   → RBB: {self.visualizer.colorize(f'{rbb}', 'green')} ✓")
        
        print("\n" + self.visualizer.colorize("2. CPA (Central Processing Axis) Számítás", 'bold'))
        print("   Formula: CPA = (Accuracy × Consistency × Adaptability)^(1/3)")
        
        accuracy = 8.5
        consistency = 8.7
        adaptability = 8.3
        cpa = self.calc.compute_cpa(accuracy, consistency, adaptability)
        
        print(f"   Accuracy: {self.visualizer.colorize(f'{accuracy}', 'cyan')}")
        print(f"   Consistency: {self.visualizer.colorize(f'{consistency}', 'cyan')}")
        print(f"   Adaptability: {self.visualizer.colorize(f'{adaptability}', 'cyan')}")
        print(f"   → CPA: {self.visualizer.colorize(f'{cpa}', 'green')} ✓")
        
        print("\n" + self.visualizer.colorize("3. tofu (Truth-Over-Fiction Unit) - KRITIKUS!", 'bold'))
        print("   Formula: tofu = Fictional_Elements / Total_Elements")
        print("   Cél: tofu = 0 (ZERO HALLUCINATION)")
        
        fictional = 0
        total = 100
        tofu = self.calc.compute_tofu(fictional, total)
        
        print(f"   Fictional Elements: {self.visualizer.colorize(f'{fictional}', 'green')}")
        print(f"   Total Elements: {self.visualizer.colorize(f'{total}', 'cyan')}")
        print(f"   → tofu: {self.visualizer.colorize(f'{tofu}', 'green')} ✓✓✓ PERFECT!")
        
        input("\n" + self.visualizer.colorize("Nyomj ENTER-t a folytatáshoz...", 'yellow'))
    
    def demo_single_cycle(self):
        """Egyetlen CRCL ciklus bemutatása"""
        self.print_header("🔄 EGYETLEN CRCL CIKLUS DEMO")
        
        problem = {
            'type': 'demo',
            'description': 'Interactive demo problem',
            'goal': 'Demonstrate CRCL capabilities',
            'constraints': ['tofu = 0', 'RBB >= 9.2']
        }
        
        print("\n" + self.visualizer.colorize("📋 Probléma Definíció:", 'bold'))
        print(json.dumps(problem, indent=2))
        
        print("\n" + self.visualizer.colorize("⏳ Ciklus futtatása...", 'yellow'))
        time.sleep(1)
        
        result = self.engine.execute_full_cycle(problem)
        
        print("\n" + self.visualizer.colorize("✅ Ciklus Befejezve!", 'green'))
        
        # Metrikák megjelenítése
        self.visualizer.display_metrics(result['meta_cognitive'], "Ciklus Eredmények")
        
        # Rövid összefoglaló
        print(f"\n{self.visualizer.colorize('📊 Összefoglaló:', 'bold')}")
        print(f"  • Futtatott hurkok: {self.visualizer.colorize('4', 'cyan')} (A, B, C, D)")
        print(f"  • Kvantum explorációk: {self.visualizer.colorize(str(result['quantum_exploration']), 'cyan')}")
        print(f"  • Végső RBB: {self.visualizer.colorize(f\"{result['meta_cognitive'].rbb:.3f}\", 'green')}")
        print(f"  • tofu érték: {self.visualizer.colorize(f\"{result['meta_cognitive'].tofu:.3f}\", 'green')} (ZERO ✓)")
        print(f"  • Optimális: {self.visualizer.colorize('IGEN ✓' if result['optimal'] else 'Még nem', 'green' if result['optimal'] else 'yellow')}")
        
        self.session_data.append({
            'timestamp': datetime.now().isoformat(),
            'type': 'single_cycle',
            'result': result
        })
        
        input("\n" + self.visualizer.colorize("Nyomj ENTER-t a folytatáshoz...", 'yellow'))
    
    def demo_convergence(self):
        """Konvergencia folyamat bemutatása"""
        self.print_header("📈 KONVERGENCIA FOLYAMAT DEMO")
        
        print("\n" + self.visualizer.colorize("Ez a demo 3 ciklust futtat és mutatja a fejlődést.", 'bold'))
        
        problem = {
            'type': 'convergence_demo',
            'description': 'Multi-cycle convergence demonstration',
            'complexity': 'high',
            'target_rbb': 9.2
        }
        
        print("\n" + self.visualizer.colorize("📋 Probléma:", 'bold'))
        for key, value in problem.items():
            print(f"  • {key}: {self.visualizer.colorize(str(value), 'cyan')}")
        
        print("\n" + self.visualizer.colorize("🚀 Konvergencia indítása...", 'yellow'))
        input("Nyomj ENTER-t a kezdéshez...")
        
        # Animált konvergencia
        self.visualizer.animate_convergence(
            self.engine, 
            problem, 
            max_cycles=3, 
            delay=0.8
        )
        
        # Történet elemzése
        if len(self.engine.loop_history) > 0:
            print("\n" + self.visualizer.colorize("📊 Fejlődési Analízis:", 'bold'))
            
            rbb_values = [state.metrics.rbb for state in self.engine.loop_history 
                         if state.loop_class.value == 'D']  # Meta-kognitív hurkok
            
            if len(rbb_values) > 1:
                improvement = rbb_values[-1] - rbb_values[0]
                improvement_pct = (improvement / rbb_values[0]) * 100
                
                print(f"  • Kezdeti RBB: {self.visualizer.colorize(f'{rbb_values[0]:.3f}', 'cyan')}")
                print(f"  • Végső RBB: {self.visualizer.colorize(f'{rbb_values[-1]:.3f}', 'green')}")
                print(f"  • Javulás: {self.visualizer.colorize(f'+{improvement:.3f}', 'green')} ({improvement_pct:+.1f}%)")
        
        self.session_data.append({
            'timestamp': datetime.now().isoformat(),
            'type': 'convergence',
            'cycles': len(self.engine.loop_history)
        })
        
        input("\n" + self.visualizer.colorize("Nyomj ENTER-t a folytatáshoz...", 'yellow'))
    
    def demo_custom_problem(self):
        """Felhasználó által definiált probléma"""
        self.print_header("🎨 EGYEDI PROBLÉMA DEMO")
        
        print("\n" + self.visualizer.colorize("Adj meg egy saját problémát!", 'bold'))
        print(self.visualizer.colorize("(vagy nyomj ENTER-t az alapértelmezetthez)", 'yellow'))
        
        print("\nProbléma típusa (pl. optimization, analysis, creative):")
        problem_type = input("  > ").strip() or "optimization"
        
        print("\nProbléma leírása:")
        description = input("  > ").strip() or "Custom CRCL problem solving"
        
        print("\nCélérték RBB-hez (alapértelmezett: 9.2):")
        target_str = input("  > ").strip()
        target_rbb = float(target_str) if target_str else 9.2
        
        problem = {
            'type': problem_type,
            'description': description,
            'target_rbb': target_rbb,
            'user_defined': True
        }
        
        print("\n" + self.visualizer.colorize("📋 A te problémád:", 'bold'))
        print(json.dumps(problem, indent=2))
        
        print("\n" + self.visualizer.colorize("🔄 Feldolgozás...", 'yellow'))
        time.sleep(1)
        
        result = self.engine.execute_full_cycle(problem)
        
        self.visualizer.display_metrics(result['meta_cognitive'], "Egyedi Probléma Eredmények")
        
        print(f"\n{self.visualizer.colorize('✨ Gratulálok!', 'green')}")
        print(f"A CRCL sikeresen feldolgozta a problémádat!")
        print(f"RBB elért: {self.visualizer.colorize(f\"{result['meta_cognitive'].rbb:.3f}\", 'green')} "
              f"/ Cél: {target_rbb:.2f}")
        
        self.session_data.append({
            'timestamp': datetime.now().isoformat(),
            'type': 'custom_problem',
            'problem': problem,
            'result': result
        })
        
        input("\n" + self.visualizer.colorize("Nyomj ENTER-t a folytatáshoz...", 'yellow'))
    
    def demo_metrics_comparison(self):
        """Metrikák összehasonlítása különböző konfigurációkkal"""
        self.print_header("⚖️ METRIKA ÖSSZEHASONLÍTÁS DEMO")
        
        print("\n" + self.visualizer.colorize("Három különböző konfiguráció összehasonlítása:", 'bold'))
        
        configs = [
            {'name': 'Konzervatív', 'truth': 8.0, 'believability': 8.0, 'accuracy': 8.0, 'consistency': 8.5, 'adaptability': 7.5},
            {'name': 'Kiegyensúlyozott', 'truth': 9.0, 'believability': 9.0, 'accuracy': 8.5, 'consistency': 8.5, 'adaptability': 8.5},
            {'name': 'Agresszív', 'truth': 9.5, 'believability': 9.8, 'accuracy': 9.0, 'consistency': 9.2, 'adaptability': 9.5}
        ]
        
        results = []
        
        for config in configs:
            print(f"\n{self.visualizer.colorize(f\"📊 {config['name']} Konfiguráció:\", 'bold')}")
            
            rbb = self.calc.compute_rbb(config['truth'], config['believability'])
            cpa = self.calc.compute_cpa(config['accuracy'], config['consistency'], config['adaptability'])
            
            print(f"  RBB: {self.visualizer.colorize(f'{rbb:.3f}', 'cyan')} "
                  f"{'✓' if rbb >= 9.2 else '⚠'}")
            print(f"  CPA: {self.visualizer.colorize(f'{cpa:.3f}', 'cyan')} "
                  f"{'✓' if cpa >= 8.5 else '⚠'}")
            
            results.append({
                'name': config['name'],
                'rbb': rbb,
                'cpa': cpa
            })
        
        # Összehasonlító táblázat
        print(f"\n{self.visualizer.colorize('📋 Összehasonlító Táblázat:', 'bold')}")
        print(f"  {'Konfig':<15} │ {'RBB':<8} │ {'CPA':<8} │ {'Státusz':<10}")
        print(self.visualizer.colorize("  " + "─" * 50, 'cyan'))
        
        for result in results:
            status = "✓ Optimal" if result['rbb'] >= 9.2 and result['cpa'] >= 8.5 else "⚠ Sub-opt"
            status_color = 'green' if '✓' in status else 'yellow'
            
            print(f"  {result['name']:<15} │ {result['rbb']:8.3f} │ {result['cpa']:8.3f} │ "
                  f"{self.visualizer.colorize(status, status_color)}")
        
        # Legjobb kiválasztása
        best = max(results, key=lambda x: x['rbb'] + x['cpa'])
        print(f"\n{self.visualizer.colorize('🏆 Legjobb Konfiguráció:', 'green')} {best['name']}")
        
        input("\n" + self.visualizer.colorize("Nyomj ENTER-t a folytatáshoz...", 'yellow'))
    
    def export_session_data(self):
        """Munkamenet adatok exportálása"""
        self.print_header("💾 ADATOK EXPORTÁLÁSA")
        
        if not self.session_data:
            print("\n" + self.visualizer.colorize("⚠ Nincs exportálható adat!", 'yellow'))
            print("Futtass előbb néhány demót.")
            input("\nNyomj ENTER-t...")
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # JSON export
        json_file = f"crcl_session_{timestamp}.json"
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(self.session_data, f, indent=2, default=str)
        
        print(f"\n✅ JSON export: {self.visualizer.colorize(json_file, 'green')}")
        
        # CSV export (egyszerűsített)
        csv_file = f"crcl_session_{timestamp}.csv"
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Timestamp', 'Type', 'Details'])
            
            for entry in self.session_data:
                writer.writerow([
                    entry['timestamp'],
                    entry['type'],
                    json.dumps({k: v for k, v in entry.items() if k not in ['timestamp', 'type']})
                ])
        
        print(f"✅ CSV export: {self.visualizer.colorize(csv_file, 'green')}")
        
        print(f"\n📊 Összesen {len(self.session_data)} esemény exportálva.")
        
        input("\n" + self.visualizer.colorize("Nyomj ENTER-t a folytatáshoz...", 'yellow'))
    
    def show_tutorial(self):
        """Részletes tutorial megjelenítése"""
        self.print_header("📚 CRCL TUTORIAL")
        
        tutorial_steps = [
            ("1️⃣ CRCL Alapok", [
                "A CRCL egy önfejlesztő AI rendszer",
                "4 hurok osztállyal: Perception, Evaluation, Correction, Meta-Cognitive",
                "Cél: Zéró hallucináció (tofu=0) + Magas RBB (≥9.2)",
                "Háromrétegű motor: Quantum-Meta-Real szinergia"
            ]),
            ("2️⃣ Metrikák Megértése", [
                "RBB: Valóság és hitelesség egyensúlya",
                "CPA: Központi feldolgozás hatékonysága",
                "CGAS: Kognitív földelés és stabilitás",
                "tofu: Hallucináció mértéke (MINDIG 0!)",
                "SR: Stabilitási arány"
            ]),
            ("3️⃣ Működés Menete", [
                "1. Probléma definiálása",
                "2. CRCL motor inicializálása",
                "3. Ciklusok futtatása (Perception → Evaluation → Correction → Meta)",
                "4. Konvergálás az optimális állapothoz",
                "5. Eredmények értékelése"
            ]),
            ("4️⃣ Gyakorlati Használat", [
                "Használd a CRCLEngine osztályt",
                "Definiálj egy problem dictionary-t",
                "Hívd meg a converge() metódust",
                "Elemezd az eredményeket",
                "Exportáld az adatokat elemzéshez"
            ])
        ]
        
        for title, steps in tutorial_steps:
            print(f"\n{self.visualizer.colorize(title, 'bold')}")
            print(self.visualizer.colorize('─' * 60, 'cyan'))
            for step in steps:
                print(f"  • {step}")
            
            input("\n" + self.visualizer.colorize("Nyomj ENTER-t a folytatáshoz...", 'yellow'))
    
    def run(self):
        """Fő menü futtatása"""
        while True:
            self.print_header("🧠 CRCL INTERACTIVE DEMO 🧠")
            
            print(self.visualizer.colorize("\nCognitive Recursive Convergence Loop", 'cyan'))
            print(self.visualizer.colorize("Interactive Demonstration System", 'cyan'))
            print(f"\nSzerző: {self.visualizer.colorize('Czink Ákos József', 'bold')}")
            print(f"Projekt: {self.visualizer.colorize('SECUND AI Research Initiative', 'bold')}")
            
            options = [
                "📚 Tutorial - CRCL alapok megértése",
                "🧮 Metrika Számítások Demo",
                "🔄 Egyetlen CRCL Ciklus Demo",
                "📈 Konvergencia Folyamat Demo",
                "🎨 Egyedi Probléma Megoldása",
                "⚖️ Metrika Összehasonlítás",
                "💾 Munkamenet Adatok Exportálása",
                "❌ Kilépés"
            ]
            
            self.print_menu("📋 Válassz egy opciót:", options)
            
            choice = input("\n  Választás (1-8): ").strip()
            
            if choice == '1':
                self.show_tutorial()
            elif choice == '2':
                self.demo_basic_metrics()
            elif choice == '3':
                self.demo_single_cycle()
            elif choice == '4':
                self.demo_convergence()
            elif choice == '5':
                self.demo_custom_problem()
            elif choice == '6':
                self.demo_metrics_comparison()
            elif choice == '7':
                self.export_session_data()
            elif choice == '8':
                print(f"\n{self.visualizer.colorize('👋 Köszönjük, hogy kipróbáltad a CRCL rendszert!', 'green')}")
                print(f"{self.visualizer.colorize('✨ További információ: akos.czink@gmail.com', 'cyan')}\n")
                break
            else:
                print(f"\n{self.visualizer.colorize('⚠ Érvénytelen választás!', 'red')}")
                time.sleep(1)


def main():
    """Főprogram"""
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                    🌟 WELCOME TO CRCL INTERACTIVE DEMO 🌟                    ║
║                                                                              ║
║              Experience the power of Cognitive Recursive                     ║
║                    Convergence Loop firsthand!                               ║
║                                                                              ║
║                         Press ENTER to begin...                              ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)
    
    input()
    
    demo = CRCLInteractiveDemo()
    
    try:
        demo.run()
    except KeyboardInterrupt:
        print("\n\n" + demo.visualizer.colorize("⚠ Demo megszakítva!", 'yellow'))
        print(demo.visualizer.colorize("👋 Viszlát!", 'cyan'))
    except Exception as e:
        print(f"\n\n{demo.visualizer.colorize('❌ Hiba történt:', 'red')} {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
