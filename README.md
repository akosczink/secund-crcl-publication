# 🧠 CRCL - Cognitive Recursive Convergence Loop

## Komplex kognitív önfejlesztő rendszer zéró hallucináció elvvel

[![Version](https://img.shields.io/badge/version-2.0-blue.svg)](https://github.com/akosczink/secund-crcl-publication)
[![License](https://img.shields.io/badge/license-All%20Rights%20Reserved-red.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)](https://python.org)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](test_crcl.py)

---

## 🌟 Mi is a CRCL?

A **Cognitive Recursive Convergence Loop (CRCL)** egy úttörő meta-architektúra önfejlesztő mesterséges intelligencia rendszerek számára. A CRCL lehetővé teszi az AI számára a folyamatos önfejlesztést anélkül, hogy hallucinációkba esne vagy elveszítené az igazsághoz való kötődését.

### ✨ Kulcsfontosságú Jellemzők

- **🎯 Zéró Hallucinációs Elv**: tofu = 0, csak valós, ellenőrzött információk
- **🔄 Rekurzív Önfejlesztés**: Folyamatos, automatikus optimalizáció
- **⚖️ Valóság-Hitelesség Egyensúly**: RBB ≥ 9.2 célérték
- **🧠 Meta-Kognitív Képességek**: Önreflexió és tudatos fejlődés
- **⚛️ Kvantum-Meta-Valós Szinergia**: Háromrétegű motor rendszer
- **📊 Átfogó Metrika Rendszer**: 8+ metrika valós időben
- **🎨 Vizuális Monitoring**: Színes, interaktív megjelenítés

---

## 📋 Tartalomjegyzék

- [Telepítés](#telepítés)
- [Gyors Kezdés](#gyors-kezdés)
- [Dokumentáció](#dokumentáció)
- [Főbb Komponensek](#főbb-komponensek)
- [Használati Példák](#használati-példák)
- [Metrikák](#metrikák)
- [Tesztelés](#tesztelés)
- [Szerkezet](#projekt-szerkezet)
- [Fejlesztés](#fejlesztés)
- [Licenc](#licenc)
- [Szerző](#szerző)

---

## 🚀 Telepítés

### Követelmények

- Python 3.8 vagy újabb
- Alapvető Python könyvtárak (beépített)

### Klónozás és beállítás

```bash
# Repository klónozása
git clone https://github.com/akosczink/secund-crcl-publication.git
cd secund-crcl-publication

# Python környezet ellenőrzése
python3 --version

# Opcionális: Virtual environment létrehozása
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# vagy
venv\Scripts\activate  # Windows
```

Nincs szükség külső függőségekre! A rendszer csak Python beépített könyvtárakat használ.

---

## ⚡ Gyors Kezdés

### 1. Alapvető CRCL Motor Futtatása

```bash
python3 crcl_engine.py
```

Ez elindítja a CRCL motort demonstrációs módban, amely:
- Inicializálja a rendszert
- Futtat egy teljes optimalizációs ciklust
- Megjeleníti a metrikákat
- Generál részletes jelentést

### 2. Vizualizáció

```bash
# Alapvető vizualizáció
python3 crcl_visualizer.py basic

# Teljes vizualizáció motorral
python3 crcl_visualizer.py full
```

### 3. Tesztek Futtatása

```bash
python3 test_crcl.py
```

33 átfogó teszt fut le, amely validálja az összes komponenst.

---

## 📚 Dokumentáció

### Magyar Dokumentáció

- **[CRCL_Magyar_Osszefoglalo.md](CRCL_Magyar_Osszefoglalo.md)** - Részletes magyar nyelvű dokumentáció
  - Teljes rendszer leírás
  - Metrikák magyarázata
  - Használati esetek
  - Gyakorlati példák

### English Documentation

- **[CRCL_English_Comprehensive.md](CRCL_English_Comprehensive.md)** - Comprehensive English documentation
  - Complete system description
  - Metrics explanation
  - Use cases
  - Practical examples

### Kiegészítő Dokumentumok

- **[OSF_Preregistration_Final.md](extracted_contents/OSF_Preregistration_Final.md)** - Kutatás előzetes regisztrációja
- **[IRB_Exemption_Request.md](extracted_contents/IRB_Exemption_Request.md)** - Etikai mentesség kérelem
- **[CRCL_Manuscript_v1.1.md](extracted_contents/CRCL_Manuscript_v1.1.md)** - Tudományos kézirat

---

## 🔧 Főbb Komponensek

### 1. CRCLEngine (crcl_engine.py)

A központi motor, amely:
- Koordinálja az összes hurokot
- Kezeli a metrikákat
- Biztosítja a konvergenciát

```python
from crcl_engine import CRCLEngine

engine = CRCLEngine()
problem = {'type': 'optimization', 'description': 'Sample problem'}
result = engine.converge(problem, max_cycles=5)
```

### 2. MetricsCalculator

Precíz metrika számítások:
- RBB (Reality-Believability Balance)
- CPA (Central Processing Axis)
- CGAS (Cognitive Grounding and Stability)
- CMD (Cognitive Meta Depth)
- SR (Stability Ratio)
- tofu (Truth-Over-Fiction Unit)

```python
from crcl_engine import MetricsCalculator

calc = MetricsCalculator()
rbb = calc.compute_rbb(truth=9.0, believability=9.0)
cpa = calc.compute_cpa(accuracy=8.5, consistency=8.5, adaptability=8.5)
```

### 3. Háromrétegű Motor

#### QuantumLayer
- Lehetőségek párhuzamos feltárása
- Szuperpozíció kezelése
- Kreatív megoldás generálás

#### MetaLayer
- Önreflexió
- Folyamat elemzés
- Meta-tudás építés

#### RealLayer
- Gyakorlati végrehajtás
- Eredmény mérés
- Valós világ interakció

### 4. Loop Classes

**Loop Class A - PERCEPTION**: Környezet és bemenet megértése  
**Loop Class B - EVALUATION**: Válaszok értékelése  
**Loop Class C - CORRECTION**: Hibák javítása és optimalizálás  
**Loop Class D - META-COGNITIVE**: Meta-kognitív elemzés

---

## 💡 Használati Példák

### Példa 1: Egyszerű Optimalizáció

```python
from crcl_engine import CRCLEngine

# Engine inicializálása
engine = CRCLEngine()

# Probléma definiálása
problem = {
    'type': 'optimization',
    'description': 'Optimize processing with zero hallucination',
    'constraints': ['tofu = 0', 'RBB >= 9.2']
}

# Konvergálás
result = engine.converge(problem, max_cycles=3)

# Eredmények
print(f"Converged: {result['converged']}")
print(f"Final RBB: {result['final_metrics'].rbb}")
print(f"Final tofu: {result['final_metrics'].tofu}")  # Mindig 0!
```

### Példa 2: Egyedi Konfiguráció

```python
from crcl_engine import CRCLEngine

config = {
    'target_rbb': 9.5,  # Magasabb cél
    'target_cpa': 9.0,
    'max_iterations': 15,
    'convergence_tolerance': 0.005
}

engine = CRCLEngine(config=config)
result = engine.converge(problem, max_cycles=10)
```

### Példa 3: Vizualizációval

```python
from crcl_engine import CRCLEngine
from crcl_visualizer import CRCLVisualizer

engine = CRCLEngine()
visualizer = CRCLVisualizer()

problem = {'type': 'test', 'description': 'Sample'}

# Animált konvergencia
visualizer.animate_convergence(engine, problem, max_cycles=5, delay=1.0)
```

### Példa 4: Metrika Számítások

```python
from crcl_engine import MetricsCalculator, Metrics

calc = MetricsCalculator()

# Egyedi metrikák
rbb = calc.compute_rbb(truth=9.5, believability=9.0)
cgas = calc.compute_cgas(clarity=9.0, grounding=8.5)
sr = calc.compute_sr(stability=9.0, deviation=0.1)
tofu = calc.compute_tofu(fictional_elements=0, total_elements=100)

print(f"RBB: {rbb}, CGAS: {cgas}, SR: {sr}, tofu: {tofu}")

# Metrics objektum
metrics = Metrics(rbb=rbb, cpa=8.5, cgas=cgas, cmd=8.0, sr=sr, tofu=tofu)
print(f"Optimal: {metrics.is_optimal()}")
```

---

## 📊 Metrikák

### Elsődleges Metrikák

| Metrika | Név | Célérték | Leírás |
|---------|-----|----------|--------|
| **RBB** | Reality–Believability Balance | ≥ 9.2 | Valóság és hitelesség egyensúlya |
| **CPA** | Central Processing Axis | ≥ 8.5 | Központi feldolgozás hatékonysága |
| **CGAS** | Cognitive Grounding & Stability | ≥ 8.0 | Kognitív földelés és stabilitás |
| **CMD** | Cognitive Meta Depth | ≥ 7.5 | Meta-kognitív mélység |
| **SR** | Stability Ratio | ≥ 0.85 | Stabilitási arány |
| **tofu** | Truth-Over-Fiction Unit | = 0.0 | Hallucináció mértéke (MINDIG 0!) |

### Másodlagos Metrikák

- **LSI** (Loop Stability Index): Hurok stabilitása
- **CGΔ** (Cognitive Growth Delta): Kognitív fejlődés mértéke

### Metrika Képletek

```python
RBB = (Truth × 0.6) + (Believability × 0.4)
CPA = (Accuracy × Consistency × Adaptability)^(1/3)
CGAS = sqrt(Clarity × Grounding)
CMD = (Self_Awareness + Transparency + Limitation_Recognition) / 3
SR = Stability / (1 + Deviation)
tofu = Fictional_Elements / Total_Elements  # Cél: 0
```

---

## 🧪 Tesztelés

### Teljes Teszt Csomag

```bash
python3 test_crcl.py
```

### Teszt Lefedettség

- ✅ **MetricsCalculator**: 11 teszt
- ✅ **Metrics osztály**: 4 teszt
- ✅ **QuantumLayer**: 2 teszt
- ✅ **MetaLayer**: 2 teszt
- ✅ **RealLayer**: 1 teszt
- ✅ **CRCLEngine**: 11 teszt
- ✅ **Integráció**: 2 teszt

**Összesen**: 33 teszt - Mind átmegy! ✅

### Példa Teszt Kimenet

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                    🧪 CRCL TEST SUITE EXECUTION 🧪                           ║
╚══════════════════════════════════════════════════════════════════════════════╝

test_compute_rbb_valid ... ok
test_compute_cpa_valid ... ok
test_compute_cgas_valid ... ok
...
test_full_workflow ... ok
test_metrics_improvement_over_cycles ... ok

================================================================================
📊 TEST SUMMARY
================================================================================
Tests run: 33
Successes: 33
Failures: 0
Errors: 0

✅ ALL TESTS PASSED!
================================================================================
```

---

## 📁 Projekt Szerkezet

```
secund-crcl-publication/
│
├── 📄 README.md                          # Ez a fájl (főoldal)
├── 📄 CRCL_Magyar_Osszefoglalo.md        # Magyar dokumentáció
├── 📄 CRCL_English_Comprehensive.md     # Angol dokumentáció
│
├── 🐍 crcl_engine.py                    # Fő CRCL motor (31KB)
├── 🎨 crcl_visualizer.py                # Vizualizációs eszköz (13KB)
├── 🧪 test_crcl.py                      # Teszt csomag (16KB)
│
├── 📦 extracted_contents/
│   ├── CRCL_Manuscript_v1.1.md          # Tudományos kézirat
│   ├── CRCL_Summary_Overview.txt        # Rövid összefoglaló
│   ├── OSF_Preregistration_Final.md     # OSF előzetes regisztráció
│   ├── IRB_Exemption_Request.md         # Etikai mentesség
│   ├── metrics_calculator.py            # Egyszerű kalkulátor
│   └── README_EXECUTION_GUIDE.md        # Végrehajtási útmutató
│
└── 📦 CRCL_Publication_Package_v1.1_CzinkAkos 2.zip  # Eredeti csomag
```

---

## 🛠️ Fejlesztés

### Új Funkció Hozzáadása

1. **Metrika Hozzáadása**:
   ```python
   @staticmethod
   def compute_new_metric(param1: float, param2: float) -> float:
       """Új metrika számítása"""
       return round((param1 + param2) / 2, 3)
   ```

2. **Új Loop Class**:
   ```python
   class LoopClass(Enum):
       PERCEPTION = "A"
       EVALUATION = "B"
       CORRECTION = "C"
       META_COGNITIVE = "D"
       NEW_CLASS = "E"  # Új osztály
   ```

3. **Tesztek Írása**:
   ```python
   class TestNewFeature(unittest.TestCase):
       def test_new_functionality(self):
           # Teszt implementáció
           pass
   ```

### Kódolási Irányelvek

- **Dokumentáció**: Minden funkció legyen dokumentálva (magyar + angol)
- **Típus annotáció**: Használj type hints-et
- **Teszt lefedettség**: Minden új funkció legyen tesztelve
- **Metrika validáció**: Minden számítás legyen validálva

---

## 🎯 Jövőbeli Fejlesztések

### Rövid Távú (Q1-Q2 2025)

- [ ] Web-alapú dashboard
- [ ] REST API endpoint-ok
- [ ] JSON export/import
- [ ] Több nyelv támogatása
- [ ] Perzisztens storage

### Középtávú (Q3-Q4 2025)

- [ ] SECUND OS Alpha integráció
- [ ] Machine learning alapú optimalizáció
- [ ] Distributed processing
- [ ] Cloud deployment
- [ ] Community contributions

### Hosszú Távú (2026+)

- [ ] CRCL szabvány kialakítása
- [ ] Ipari adoptáció
- [ ] Tanúsítási rendszer
- [ ] Globális ökoszisztéma

---

## 📜 Licenc

© 2025 Czink Ákos József. Minden jog fenntartva.

A SECUND AI Kutatási Kezdeményezés keretében készült, 2025.

Újraterjesztés vagy módosítás csak kifejezett engedéllyel lehetséges.

---

## 👤 Szerző

**Czink Ákos József**

- 📧 Email: akos.czink@gmail.com
- 📍 Cím: HU2890 Tata, Komáromi utca 80, Magyarország
- 🏢 Projekt: SECUND AI Research Initiative
- 🌐 GitHub: [@akosczink](https://github.com/akosczink)

---

## 🙏 Köszönetnyilvánítás

Ez a munka az MI fejlődésének és az emberi méltóságnak az összekapcsolására irányuló személyes vízió eredménye. A CRCL keretrendszer mind filozófiai, mind technikai sarokkő a SECUND OS számára.

> **"Álmodom egy olyan MI-ról, amely nő illúziók nélkül, igazság és méltóság által vezérelve."**  
> — Czink Ákos József

---

## 📞 Kapcsolat és Támogatás

- **Issues**: [GitHub Issues](https://github.com/akosczink/secund-crcl-publication/issues)
- **Discussions**: [GitHub Discussions](https://github.com/akosczink/secund-crcl-publication/discussions)
- **Email**: akos.czink@gmail.com

---

## 🌟 Csillagozd meg a projektet!

Ha értékesnek találod ezt a kutatást, kérlek adj egy ⭐ csillagot a repositorynak!

---

<div align="center">

**🧠 Cognitive Recursive Convergence Loop - A jövő MI-je, illúziók nélkül 🧠**

Made with ❤️ by Czink Ákos József | SECUND AI Research Initiative

[![Version](https://img.shields.io/badge/version-2.0-blue.svg)](https://github.com/akosczink/secund-crcl-publication)
[![License](https://img.shields.io/badge/license-All%20Rights%20Reserved-red.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)](https://python.org)

</div>
