# 📚 CRCL Gyakorlati Példák és Tutorialok
## Comprehensive Practical Examples and Tutorials

**Szerző:** Czink Ákos József  
**Projekt:** SECUND AI Research Initiative  
**Verzió:** 2.0 - Teljes Tutorial Csomag

---

## 📋 Tartalomjegyzék

1. [Kezdő Tutorial](#1-kezdő-tutorial)
2. [Haladó Példák](#2-haladó-példák)
3. [Speciális Használati Esetek](#3-speciális-használati-esetek)
4. [Hibakeresés és Optimalizálás](#4-hibakeresés-és-optimalizálás)
5. [Valós Projektek](#5-valós-projektek)
6. [Best Practices](#6-best-practices)

---

## 1️⃣ Kezdő Tutorial

### 1.1 Az Első CRCL Program

```python
#!/usr/bin/env python3
"""
Az első CRCL programod
Your first CRCL program
"""

from crcl_engine import CRCLEngine

# 1. Motor inicializálása
print("🚀 CRCL Engine inicializálása...")
engine = CRCLEngine()

# 2. Probléma definiálása
problem = {
    'type': 'hello_world',
    'description': 'Az első CRCL futtatás',
    'goal': 'Megérteni a CRCL alapokat'
}

# 3. Egyetlen ciklus futtatása
print("\n🔄 Ciklus futtatása...")
result = engine.execute_full_cycle(problem)

# 4. Eredmények megjelenítése
print(f"\n✅ Siker!")
print(f"RBB: {result['final_metrics'].rbb:.3f}")
print(f"tofu: {result['final_metrics'].tofu:.3f} (Zero hallucination ✓)")
print(f"Optimális: {result['optimal']}")
```

**Mit tanultunk:**
- Engine inicializálás
- Probléma definiálás
- Ciklus futtatás
- Eredmények olvasása

---

### 1.2 Metrikák Számítása Manuálisan

```python
#!/usr/bin/env python3
"""
Metrika számítások manuálisan
Manual metrics calculations
"""

from crcl_engine import MetricsCalculator, Metrics

# Kalkulátor létrehozása
calc = MetricsCalculator()

# === RBB Számítás ===
print("📊 RBB (Reality-Believability Balance)")
truth = 9.0          # Mennyire igaz (0-10)
believability = 9.2  # Mennyire hihető (0-10)

rbb = calc.compute_rbb(truth, believability)
print(f"   Truth: {truth}, Believability: {believability}")
print(f"   → RBB: {rbb}")
print(f"   Cél (≥9.2): {'✓ ELÉRVE' if rbb >= 9.2 else '⚠ Még nem'}\n")

# === CPA Számítás ===
print("⚙️ CPA (Central Processing Axis)")
accuracy = 8.5      # Pontosság
consistency = 8.7   # Következetesség
adaptability = 8.3  # Alkalmazkodóképesség

cpa = calc.compute_cpa(accuracy, consistency, adaptability)
print(f"   Accuracy: {accuracy}")
print(f"   Consistency: {consistency}")
print(f"   Adaptability: {adaptability}")
print(f"   → CPA: {cpa} (geometrikus átlag)")
print(f"   Cél (≥8.5): {'✓ ELÉRVE' if cpa >= 8.5 else '⚠ Még nem'}\n")

# === tofu Számítás - KRITIKUS ===
print("🎯 tofu (Truth-Over-Fiction Unit) - ZERO HALLUCINATION")
fictional = 0   # Kitalált elemek száma
total = 100     # Összes elem száma

tofu = calc.compute_tofu(fictional, total)
print(f"   Fictional: {fictional}, Total: {total}")
print(f"   → tofu: {tofu}")
print(f"   Cél (=0.0): {'✅ PERFECT!' if tofu == 0.0 else '❌ HALLUCINÁCIÓ!'}\n")

# === Teljes Metrics objektum ===
print("📦 Teljes Metrics Objektum")
metrics = Metrics(
    rbb=rbb,
    cpa=cpa,
    cgas=calc.compute_cgas(clarity=9.0, grounding=8.5),
    cmd=calc.compute_cmd(8.0, 8.5, 8.0),
    sr=calc.compute_sr(stability=9.0, deviation=0.1),
    tofu=tofu
)

print(metrics)
print(f"\n🎯 Minden metrika optimális: {metrics.is_optimal()}")
```

**Mit tanultunk:**
- Egyedi metrikák számítása
- Metrika értelmezése
- Célértékek ellenőrzése
- Metrics objektum használata

---

### 1.3 Vizualizáció Használata

```python
#!/usr/bin/env python3
"""
Vizualizáció használata
Using visualization tools
"""

from crcl_engine import CRCLEngine, Metrics
from crcl_visualizer import CRCLVisualizer

# Inicializálás
engine = CRCLEngine()
visualizer = CRCLVisualizer()

# Probléma megoldása
problem = {'type': 'visualization_demo', 'goal': 'Beautiful output'}
result = engine.execute_full_cycle(problem)

# === Metrikák vizualizálása ===
print("\n1️⃣ Metrikák Megjelenítése:")
visualizer.display_metrics(
    result['meta_cognitive'],
    title="Ciklus Eredmények"
)

# === Hurok történet ===
print("\n2️⃣ Hurok Történet:")
visualizer.display_loop_history(engine.loop_history)

# === Konvergencia grafikon ===
print("\n3️⃣ Konvergencia Grafikon:")
visualizer.display_convergence_graph(engine.loop_history, 'rbb')

# === Összehasonlító táblázat ===
print("\n4️⃣ Összehasonlítás:")
# Futtassunk még egy ciklust
engine.execute_full_cycle(problem)
visualizer.display_comparison_table(engine.loop_history)
```

**Mit tanultunk:**
- Vizualizációs eszközök használata
- Színes kimenet
- Grafikonok ASCII művészettel
- Összehasonlító elemzések

---

## 2️⃣ Haladó Példák

### 2.1 Egyedi Konfiguráció

```python
#!/usr/bin/env python3
"""
Egyedi CRCL konfiguráció
Custom CRCL configuration
"""

from crcl_engine import CRCLEngine

# Egyedi konfiguráció definiálása
custom_config = {
    # Metrika célértékek
    'target_rbb': 9.5,      # Magasabb RBB cél
    'target_cpa': 9.0,      # Magasabb CPA cél
    'target_cgas': 8.5,     # Magasabb CGAS cél
    'target_cmd': 8.0,      # Magasabb CMD cél
    'target_sr': 0.90,      # Magasabb SR cél
    
    # Futtatási paraméterek
    'max_iterations': 20,   # Több iteráció
    'convergence_tolerance': 0.005,  # Finomabb konvergencia
    
    # Loop osztály konfigurációk
    'loop_classes': {
        'perception': {'iterations': 7},      # Több perception loop
        'evaluation': {'iterations': 5},      # Több evaluation loop
        'correction': {'iterations': 3},      # Több correction loop
        'meta': {'iterations': 10}            # Több meta loop
    }
}

# Engine létrehozása egyedi konfigurációval
print("🎨 Egyedi CRCL Engine létrehozása...")
engine = CRCLEngine(config=custom_config)

print(f"✓ Célértékek:")
print(f"  RBB: ≥{custom_config['target_rbb']}")
print(f"  CPA: ≥{custom_config['target_cpa']}")
print(f"  Max iterációk: {custom_config['max_iterations']}")

# Probléma megoldása magasabb sztenderdekkel
problem = {
    'type': 'high_precision',
    'description': 'Magas pontosságú feladat',
    'complexity': 'very_high'
}

result = engine.converge(problem, max_cycles=5)

print(f"\n🎯 Eredmények:")
print(f"  Elért RBB: {result['final_metrics'].rbb:.3f}")
print(f"  Konvergált: {result['converged']}")
print(f"  Ciklusok: {result['total_cycles']}")
```

**Mit tanultunk:**
- Egyedi konfiguráció létrehozása
- Célértékek módosítása
- Loop paraméterek beállítása
- Magasabb sztenderdek elérése

---

### 2.2 Multi-Cycle Konvergencia Analízis

```python
#!/usr/bin/env python3
"""
Többciklusos konvergencia részletes analízissel
Multi-cycle convergence with detailed analysis
"""

from crcl_engine import CRCLEngine
from crcl_visualizer import CRCLVisualizer
import statistics

# Inicializálás
engine = CRCLEngine()
visualizer = CRCLVisualizer()

problem = {
    'type': 'convergence_analysis',
    'description': 'Részletes konvergencia vizsgálat',
    'target': 'optimal_state'
}

print("📈 Konvergencia Analízis Indítása\n")

# Konvergálás 10 ciklusig
result = engine.converge(problem, max_cycles=10)

print(f"\n{'='*80}")
print("📊 RÉSZLETES ANALÍZIS")
print(f"{'='*80}\n")

# 1. Alapstatisztikák
print("1️⃣ Alapstatisztikák:")
print(f"   Összes ciklus: {result['total_cycles']}")
print(f"   Konvergált: {result['converged']}")
print(f"   Összes hurok: {len(result['history'])}")

# 2. RBB fejlődés elemzése
rbb_values = [s.metrics.rbb for s in result['history'] if s.loop_class.value == 'D']
print(f"\n2️⃣ RBB Fejlődés:")
print(f"   Kezdeti: {rbb_values[0]:.3f}")
print(f"   Végső: {rbb_values[-1]:.3f}")
print(f"   Javulás: {rbb_values[-1] - rbb_values[0]:+.3f}")
print(f"   Átlag: {statistics.mean(rbb_values):.3f}")
print(f"   Szórás: {statistics.stdev(rbb_values):.3f}")

# 3. Loop osztályok elemzése
loop_counts = {}
for state in result['history']:
    loop_class = state.loop_class.value
    loop_counts[loop_class] = loop_counts.get(loop_class, 0) + 1

print(f"\n3️⃣ Loop Osztály Megoszlás:")
for loop_class, count in sorted(loop_counts.items()):
    percentage = (count / len(result['history'])) * 100
    print(f"   Class {loop_class}: {count} futás ({percentage:.1f}%)")

# 4. Konvergencia sebesség
if len(rbb_values) > 1:
    print(f"\n4️⃣ Konvergencia Sebesség:")
    for i in range(1, min(6, len(rbb_values))):
        improvement = rbb_values[i] - rbb_values[i-1]
        print(f"   Ciklus {i}: {improvement:+.3f} RBB javulás")

# 5. Vizualizációk
print(f"\n5️⃣ Vizuális Elemzések:")
visualizer.display_convergence_graph(result['history'], 'rbb')
visualizer.display_comparison_table(result['history'])

print(f"\n{'='*80}")
print("✅ Analízis befejezve")
print(f"{'='*80}\n")
```

**Mit tanultunk:**
- Hosszú távú konvergencia
- Statisztikai elemzés
- Loop osztály megoszlás
- Fejlődés követése
- Részletes vizualizáció

---

### 2.3 Batch Processing

```python
#!/usr/bin/env python3
"""
Több probléma batch feldolgozása
Batch processing multiple problems
"""

from crcl_engine import CRCLEngine
from crcl_visualizer import CRCLVisualizer
import time

# Problémák listája
problems = [
    {
        'id': 1,
        'type': 'optimization',
        'description': 'Első optimalizálási feladat',
        'priority': 'high'
    },
    {
        'id': 2,
        'type': 'analysis',
        'description': 'Adatelemzési feladat',
        'priority': 'medium'
    },
    {
        'id': 3,
        'type': 'creative',
        'description': 'Kreatív probléma megoldás',
        'priority': 'low'
    },
    {
        'id': 4,
        'type': 'verification',
        'description': 'Eredmény verifikáció',
        'priority': 'critical'
    }
]

print(f"🔄 Batch Processing: {len(problems)} probléma\n")

# Eredmények tárolása
batch_results = []

# Feldolgozás
for i, problem in enumerate(problems, 1):
    print(f"\n{'='*60}")
    print(f"Probléma {i}/{len(problems)}: {problem['description']}")
    print(f"Prioritás: {problem['priority']}")
    print(f"{'='*60}")
    
    # Engine létrehozása minden problémához
    engine = CRCLEngine()
    
    # Időmérés
    start_time = time.time()
    
    # Futtatás
    result = engine.execute_full_cycle(problem)
    
    elapsed = time.time() - start_time
    
    # Eredmény tárolása
    batch_results.append({
        'problem': problem,
        'result': result,
        'time': elapsed,
        'success': result['optimal']
    })
    
    # Státusz
    print(f"✓ Kész: {elapsed:.3f}s | RBB: {result['final_metrics'].rbb:.3f} | "
          f"Optimális: {result['optimal']}")

# Összegzés
print(f"\n\n{'='*80}")
print("📊 BATCH ÖSSZEGZÉS")
print(f"{'='*80}\n")

successful = sum(1 for r in batch_results if r['success'])
total_time = sum(r['time'] for r in batch_results)
avg_rbb = sum(r['result']['final_metrics'].rbb for r in batch_results) / len(batch_results)

print(f"Összes probléma: {len(problems)}")
print(f"Sikeres: {successful}/{len(problems)} ({successful/len(problems)*100:.1f}%)")
print(f"Összes idő: {total_time:.3f}s")
print(f"Átlagos idő: {total_time/len(problems):.3f}s")
print(f"Átlagos RBB: {avg_rbb:.3f}")

# Részletes táblázat
print(f"\n{'ID':<5} {'Típus':<15} {'RBB':<8} {'Idő':<10} {'Státusz':<10}")
print("-" * 60)
for r in batch_results:
    print(f"{r['problem']['id']:<5} "
          f"{r['problem']['type']:<15} "
          f"{r['result']['final_metrics'].rbb:<8.3f} "
          f"{r['time']:<10.3f} "
          f"{'✓ OK' if r['success'] else '⚠ Sub':<10}")
```

**Mit tanultunk:**
- Batch feldolgozás
- Eredmények gyűjtése
- Teljesítmény mérés
- Összesített statisztikák
- Eredmények összehasonlítása

---

## 3️⃣ Speciális Használati Esetek

### 3.1 Adaptív Tanulás Szimulációja

```python
#!/usr/bin/env python3
"""
Adaptív tanulási rendszer CRCL-el
Adaptive learning system with CRCL
"""

from crcl_engine import CRCLEngine, Metrics
import random

class AdaptiveLearningSystem:
    """Adaptív tanulási rendszer"""
    
    def __init__(self):
        self.engine = CRCLEngine()
        self.knowledge_base = []
        self.performance_history = []
    
    def learn(self, topic: str, difficulty: float):
        """Tanulási folyamat szimulációja"""
        
        problem = {
            'type': 'learning',
            'topic': topic,
            'difficulty': difficulty,
            'prior_knowledge': len(self.knowledge_base)
        }
        
        print(f"\n📚 Tanulás: {topic} (Nehézség: {difficulty:.1f})")
        
        result = self.engine.execute_full_cycle(problem)
        
        # Tudás hozzáadása
        self.knowledge_base.append({
            'topic': topic,
            'mastery': result['final_metrics'].rbb,
            'timestamp': len(self.knowledge_base)
        })
        
        # Teljesítmény követése
        self.performance_history.append(result['final_metrics'].rbb)
        
        print(f"   Elsajátítás: {result['final_metrics'].rbb:.1f}/10")
        print(f"   Tudásbázis: {len(self.knowledge_base)} téma")
        
        return result
    
    def get_learning_progress(self):
        """Tanulási fejlődés lekérdezése"""
        if not self.performance_history:
            return 0.0
        
        return sum(self.performance_history) / len(self.performance_history)
    
    def recommend_next_topic(self):
        """Következő téma ajánlása"""
        avg_mastery = self.get_learning_progress()
        
        if avg_mastery >= 9.0:
            return "advanced", 0.9
        elif avg_mastery >= 7.5:
            return "intermediate", 0.6
        else:
            return "basic", 0.3

# Demo
print("🎓 ADAPTÍV TANULÁSI RENDSZER DEMO")
print("="*60)

system = AdaptiveLearningSystem()

# Tanulási path
learning_path = [
    ("Python Basics", 0.3),
    ("Data Structures", 0.5),
    ("Algorithms", 0.7),
    ("AI Fundamentals", 0.8),
    ("CRCL Theory", 0.9)
]

for topic, difficulty in learning_path:
    system.learn(topic, difficulty)

# Végső értékelés
print(f"\n\n{'='*60}")
print("📊 TANULÁSI ÉRTÉKELÉS")
print(f"{'='*60}")
print(f"Összes tanult téma: {len(system.knowledge_base)}")
print(f"Átlagos elsajátítás: {system.get_learning_progress():.2f}/10")

# Ajánlás
next_topic, next_diff = system.recommend_next_topic()
print(f"\n💡 Ajánlott következő szint: {next_topic} (Nehézség: {next_diff:.1f})")
```

**Mit tanultunk:**
- Osztály alapú használat
- Állapot követés
- Adaptív logika
- Teljesítmény analízis
- Ajánlási rendszer

---

### 3.2 Minőségellenőrzési Rendszer

```python
#!/usr/bin/env python3
"""
Automatikus minőségellenőrző rendszer
Automatic quality control system
"""

from crcl_engine import CRCLEngine, MetricsCalculator
from typing import List, Dict, Any

class QualityControlSystem:
    """Minőségellenőrzési rendszer"""
    
    def __init__(self, quality_threshold: float = 9.0):
        self.engine = CRCLEngine()
        self.calc = MetricsCalculator()
        self.threshold = quality_threshold
        self.inspections = []
    
    def inspect(self, item: Dict[str, Any]) -> Dict[str, Any]:
        """Elem minőségének ellenőrzése"""
        
        print(f"\n🔍 Ellenőrzés: {item['name']}")
        
        # CRCL alapú minőségellenőrzés
        problem = {
            'type': 'quality_control',
            'item': item,
            'standards': ['accuracy', 'completeness', 'consistency']
        }
        
        result = self.engine.execute_full_cycle(problem)
        
        # Minőségi mutatók
        quality_score = result['final_metrics'].rbb
        passed = quality_score >= self.threshold
        
        inspection_result = {
            'item': item,
            'quality_score': quality_score,
            'passed': passed,
            'metrics': result['final_metrics'],
            'issues': [] if passed else ['Quality below threshold']
        }
        
        self.inspections.append(inspection_result)
        
        # Eredmény kiírása
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"   Minőségi pontszám: {quality_score:.2f}/10")
        print(f"   Státusz: {status}")
        
        return inspection_result
    
    def generate_report(self) -> str:
        """Minőségi jelentés generálása"""
        passed = sum(1 for i in self.inspections if i['passed'])
        total = len(self.inspections)
        pass_rate = (passed / total * 100) if total > 0 else 0
        
        report = [
            "\n" + "="*60,
            "📋 MINŐSÉGELLENŐRZÉSI JELENTÉS",
            "="*60,
            f"\nEllenőrzött elemek: {total}",
            f"Megfelelő: {passed}/{total} ({pass_rate:.1f}%)",
            f"Nem megfelelő: {total - passed}/{total}",
            f"\nMinőségi küszöb: {self.threshold}/10",
            ""
        ]
        
        # Részletes lista
        report.append("Részletes eredmények:")
        report.append("-" * 60)
        
        for i, insp in enumerate(self.inspections, 1):
            status = "✓" if insp['passed'] else "✗"
            report.append(
                f"{i}. {insp['item']['name']:<20} "
                f"{status} {insp['quality_score']:.2f}/10"
            )
        
        report.append("="*60)
        
        return "\n".join(report)

# Demo
print("🏭 MINŐSÉGELLENŐRZÉSI RENDSZER DEMO")
print("="*60)

qc = QualityControlSystem(quality_threshold=8.5)

# Tesztelendő elemek
items = [
    {'name': 'Component A', 'batch': 'B001', 'type': 'electronic'},
    {'name': 'Component B', 'batch': 'B002', 'type': 'mechanical'},
    {'name': 'Component C', 'batch': 'B003', 'type': 'software'},
    {'name': 'Component D', 'batch': 'B004', 'type': 'integrated'},
]

# Ellenőrzések futtatása
for item in items:
    qc.inspect(item)

# Jelentés
print(qc.generate_report())
```

**Mit tanultunk:**
- Ipari alkalmazás
- Automatikus minőségellenőrzés
- Jelentés generálás
- Küszöbérték alapú döntés
- Batch elemzés

---

## 4️⃣ Hibakeresés és Optimalizálás

### 4.1 Debug Mód

```python
#!/usr/bin/env python3
"""
CRCL Debug és Troubleshooting
CRCL Debugging and troubleshooting
"""

from crcl_engine import CRCLEngine
import logging

# Logging beállítása
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger('CRCL_Debug')

class DebugCRCL(CRCLEngine):
    """Debug verzió extra naplózással"""
    
    def execute_full_cycle(self, problem):
        logger.info(f"🔍 Ciklus indítása: {problem}")
        
        try:
            result = super().execute_full_cycle(problem)
            logger.info(f"✅ Ciklus sikeres: RBB={result['final_metrics'].rbb:.3f}")
            return result
        except Exception as e:
            logger.error(f"❌ Hiba a ciklusban: {e}")
            raise
    
    def run_perception_loop(self, input_data):
        logger.debug("→ Perception loop kezdés")
        result = super().run_perception_loop(input_data)
        logger.debug(f"← Perception loop vége: RBB={result.metrics.rbb:.3f}")
        return result

# Használat
print("🐛 DEBUG MÓD DEMO\n")

engine = DebugCRCL()
problem = {'type': 'debug_test', 'data': 'sample'}

result = engine.execute_full_cycle(problem)

print(f"\n✅ Futtatás befejezve debug móddal")
```

### 4.2 Performance Profiling

```python
#!/usr/bin/env python3
"""
Performance profiling és optimalizálás
Performance profiling and optimization
"""

import time
import cProfile
import pstats
from crcl_engine import CRCLEngine

def profile_crcl():
    """CRCL performance profiling"""
    
    engine = CRCLEngine()
    problem = {'type': 'performance_test', 'complexity': 'high'}
    
    # Profile futtatás
    profiler = cProfile.Profile()
    profiler.enable()
    
    # Több ciklus
    for i in range(3):
        engine.execute_full_cycle(problem)
    
    profiler.disable()
    
    # Statisztikák
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative')
    
    print("\n📊 TOP 10 LASSÚ FÜGGVÉNY:")
    stats.print_stats(10)

# Egyszerű időmérés
def time_operations():
    """Műveletek időmérése"""
    
    operations = {
        'Single Cycle': lambda: CRCLEngine().execute_full_cycle({'type': 'test'}),
        'Convergence 3': lambda: CRCLEngine().converge({'type': 'test'}, max_cycles=3),
    }
    
    print("\n⏱️  IDŐMÉRÉSEK:\n")
    
    for name, operation in operations.items():
        start = time.time()
        operation()
        elapsed = time.time() - start
        print(f"{name:<20}: {elapsed:.4f}s")

# Futtatás
print("🔬 PERFORMANCE PROFILING")
print("="*60)

time_operations()
# profile_crcl()  # Részletes profiling (opcionális)
```

---

## 5️⃣ Valós Projektek

### 5.1 Kutatási Asszisztens

```python
#!/usr/bin/env python3
"""
Kutatási asszisztens CRCL-lel
Research assistant with CRCL
"""

from crcl_engine import CRCLEngine
from typing import List, Dict

class ResearchAssistant:
    """AI kutatási asszisztens"""
    
    def __init__(self):
        self.engine = CRCLEngine()
        self.findings = []
    
    def analyze_hypothesis(self, hypothesis: str, evidence: List[str]):
        """Hipotézis elemzése"""
        
        print(f"\n🔬 Hipotézis elemzése:")
        print(f"   {hypothesis}")
        
        problem = {
            'type': 'research_analysis',
            'hypothesis': hypothesis,
            'evidence': evidence,
            'method': 'systematic_review'
        }
        
        result = self.engine.execute_full_cycle(problem)
        
        # Eredmény értékelése
        confidence = result['final_metrics'].rbb / 10  # 0-1 skála
        
        finding = {
            'hypothesis': hypothesis,
            'confidence': confidence,
            'quality': result['final_metrics'].rbb,
            'hallucination_free': result['final_metrics'].tofu == 0
        }
        
        self.findings.append(finding)
        
        print(f"   Megbízhatóság: {confidence*100:.1f}%")
        print(f"   Minőség: {result['final_metrics'].rbb:.2f}/10")
        print(f"   Hallucináció-mentes: {'✓' if finding['hallucination_free'] else '✗'}")
        
        return finding

# Demo
print("🎓 KUTATÁSI ASSZISZTENS DEMO")
print("="*60)

assistant = ResearchAssistant()

# Hipotézisek tesztelése
hypotheses = [
    ("CRCL javítja az AI megbízhatóságot", ["Metrika adatok", "Teszt eredmények"]),
    ("Zéró hallucináció elérhető", ["tofu=0 bizonyítékok", "Validációs tesztek"]),
    ("Meta-kogníció növeli a hatékonyságot", ["Teljesítmény mérések", "Összehasonlító adatok"])
]

for hyp, evidence in hypotheses:
    assistant.analyze_hypothesis(hyp, evidence)

# Összegzés
print(f"\n\n📋 KUTATÁSI ÖSSZEGZÉS")
print("="*60)
avg_confidence = sum(f['confidence'] for f in assistant.findings) / len(assistant.findings)
print(f"Vizsgált hipotézisek: {len(assistant.findings)}")
print(f"Átlagos megbízhatóság: {avg_confidence*100:.1f}%")
```

---

## 6️⃣ Best Practices

### 6.1 Kód Struktúra

```python
# ✅ JÓ: Tiszta, strukturált kód
from crcl_engine import CRCLEngine

class MyApplication:
    def __init__(self):
        self.engine = CRCLEngine()
    
    def process(self, data):
        problem = self._prepare_problem(data)
        result = self.engine.execute_full_cycle(problem)
        return self._extract_results(result)
    
    def _prepare_problem(self, data):
        return {'type': 'process', 'data': data}
    
    def _extract_results(self, result):
        return {
            'rbb': result['final_metrics'].rbb,
            'optimal': result['optimal']
        }

# ❌ ROSSZ: Összekuszált, nem strukturált
engine = CRCLEngine()
result = engine.execute_full_cycle({'data': 'something'})
print(result['final_metrics'].rbb)
```

### 6.2 Hibakezelés

```python
# ✅ JÓ: Proper hibakezelés
from crcl_engine import CRCLEngine

try:
    engine = CRCLEngine()
    result = engine.execute_full_cycle(problem)
    
    if not result['optimal']:
        print("⚠ Figyelem: Nem érte el az optimális állapotot")
    
except ValueError as e:
    print(f"❌ Érvénytelen érték: {e}")
except Exception as e:
    print(f"❌ Váratlan hiba: {e}")
finally:
    print("✓ Feldolgozás befejezve")
```

### 6.3 Teljesítmény Optimalizálás

```python
# ✅ JÓ: Engine újrafelhasználás ha lehetséges
engine = CRCLEngine()

for problem in problems:
    result = engine.execute_full_cycle(problem)
    # Feldolgozás...

# ❌ ROSSZ: Új engine minden problémára
for problem in problems:
    engine = CRCLEngine()  # Lassú!
    result = engine.execute_full_cycle(problem)
```

---

## 📝 Összefoglalás

Ezek a tutorialok és példák:
- ✅ Lefedik az alapoktól a haladó használatig
- ✅ Valós projekteket mutatnak be
- ✅ Best practices-t követnek
- ✅ Hibakeresést és optimalizálást is tartalmaznak
- ✅ Mind magyar, mind angol kommentekkel

**Következő lépések:**
1. Próbáld ki az alapvető példákat
2. Módosítsd a paramétereket
3. Hozz létre saját projekteket
4. Ossz meg az eredményeket!

---

**Szerző:** Czink Ákos József  
**Email:** akos.czink@gmail.com  
**Projekt:** SECUND AI Research Initiative  
**Verzió:** 2.0

© 2025 Minden jog fenntartva
