# ONTEK UPS Technical Specifications - Complete Data Extraction

**Source:** https://ontek-rus.ru/
**Date extracted:** 2026-06-15

---

## PAGE TYPE SUMMARY

### Pages with FULL detailed technical specs (individual model pages):
1-8: PM series individual models (below)

### Pages that are CATALOG LISTINGS only (no detailed spec tables, only filter/grid with model names, power, phase, PF, battery type):
9-23: All other series pages are catalog listings linking to individual sub-model pages

---

---

## 1. ONTEK PM10/32 (External batteries 32-40 pcs)
**URL:** https://ontek-rus.ru/products/three-phase-ups/ibp-ontek-pm-10-80-kva/pm10/

| Category | Parameter | Value |
|----------|-----------|-------|
| **General** | Model | PM10/32 |
| | Power | 10 kVA / 10 kW |
| | Phase | Multi-phase (3:3, 3:1, 1:1) |
| | Parallel operation | Up to 4 UPS (common battery group possible) |
| | Parallel board | Built-in |
| | Circuit breakers | 4 pcs: main input, output, static bypass input, mechanical bypass |
| | Breaker location | Rear of UPS |
| | Connection | Dual input: main + bypass line |
| | Cable entry | Bottom rear |
| **INPUT** | Nominal voltage | 1x 220/230/240V (1ph+N) or 3x 380/400/415V (3ph+N) |
| | Voltage range | 110-300V at 50% load, 176-276V at 100% load |
| | Frequency range | 46-54 Hz or 56-64 Hz |
| | Power factor | >= 0.99 at 100% load |
| | THDi | < 4% at full linear load |
| **OUTPUT** | Output voltage | 1x 220/230/240V (1ph+N) or 3x 380/400/415V (3ph+N) |
| | Voltage regulation | +/- 1% |
| | Frequency (synced) | 46-54 Hz or 56-64 Hz |
| | Frequency (battery) | 50/60 Hz +/- 0.1 Hz |
| | Crest factor | 3:1 (max) |
| | THD | <=2% (linear load); <=5% (non-linear load) |
| | Transfer to battery | Zero |
| | Transfer to bypass | Zero |
| | Waveform (battery) | Pure sine wave |
| | Overload | 100-110% 60 min, 111-125% 10 min, 126-150% 1 min; immediate >150% |
| **BYPASS** | Nominal voltage | 1x 220/230/240V (1ph+N) or 3x 380/400/415V (3ph+N) |
| | Voltage range | -30% / +20% (adjustable) |
| | Frequency (synced) | 46-54 Hz or 56-64 Hz |
| | Overload | >130% 1 min (default); Continuous until breaker (optional) |
| **EFFICIENCY** | Online mode | 95.5% |
| | ECO mode | 98.5% |
| | Battery mode | 94.5% |
| **BATTERIES & CHARGER** | Battery type | Depends on task (external) |
| | Battery quantity | 32-40 (adjustable) |
| | Max charge current | 1-12 A (adjustable) |
| | Charge voltage | +/-13.65V x N (N = 16~20) |
| | Charge method | 3-stage |
| | Temperature compensation | Yes |
| | Cold start | Yes |
| **DISPLAY** | Display | 5" color touch LCD |
| | Info shown | UPS status, load level, battery level, input/output voltage, remaining runtime, error codes |
| **MANAGEMENT** | Interfaces | Smart RS-232 x1, USB x1 |
| | OS support | Windows, Linux, MAC |
| | Modbus card | RS485 x2, Modbus RTU |
| | Batt. temp connector | x1 (sensor included, 1 pc) |
| | Dry contacts | x1: 6 input signals, 4 output signals |
| | Optional | SNMP card, Environmental sensor (temp & humidity) |
| **PHYSICAL** | Dimensions (WxHxD) | 250 x 826 x 630 mm |
| | Net weight | 40 kg |
| | Noise at 1m | < 60 dB |
| **ENVIRONMENT** | Operating temp & humidity | 0-40 deg C, < 95% non-condensing |
| | Altitude | 0-1500 m at full load (derate 1% per 100m above) |
| **COMPLIANCE** | Certifications | EAEU TR TS 004/2011, TR TS 020/2011, ISO 9001:2015 |
| | Warranty | 3 years (standard) or extended to 5 years |

---

## 2. ONTEK PM10SB/20 (20 internal batteries)
**URL:** https://ontek-rus.ru/products/three-phase-ups/ibp-ontek-pm-10-80-kva/pm10sb-20/

Same INPUT, OUTPUT, BYPASS, EFFICIENCY, DISPLAY, MANAGEMENT, ENVIRONMENT, COMPLIANCE as PM10/32 with these differences:

| Parameter | PM10SB/20 Value |
|-----------|-----------------|
| Power | 10 kVA / 10 kW |
| Battery type | 12V / 9Ah (internal) |
| Battery quantity | 20 |
| Battery service life | Standard 5 years, 10 years optional |
| Charge voltage | +/- 13.65V x N (N = 10) |
| Recharge time | 4 hours to 90% capacity |
| Additional batteries | External battery modules can be connected |
| Dimensions | 250 x 826 x 630 mm |
| Net weight | **126 kg** |
| Noise at 1m | < 60 dB |

---

## 3. ONTEK PM10SB/32 (32 internal batteries)
**URL:** https://ontek-rus.ru/products/three-phase-ups/ibp-ontek-pm-10-80-kva/pm10sb/

Same core specs as PM10SB/20 with these differences:

| Parameter | PM10SB/32 Value |
|-----------|-----------------|
| Power | 10 kVA / 10 kW |
| Battery quantity | 32 |
| Charge voltage | +/-13.65V x N (N = 16) |
| Recharge time | 4 hours to 90% capacity |
| Dimensions | 250 x 826 x 630 mm |
| Net weight | **138 kg** |
| Noise at 1m | < 60 dB |

---

## 4. ONTEK PM15 (External batteries)
**URL:** https://ontek-rus.ru/products/three-phase-ups/ibp-ontek-pm-10-80-kva/pm15/

Same core specs as PM10/32 with these differences:

| Parameter | PM15 Value |
|-----------|------------|
| Power | 15 kVA / 15 kW |
| Battery type | Depends on task (external) |
| Battery quantity | 32-40 (adjustable) |
| Charge voltage | +/-13.65V x N (N = 16~20) |
| Max charge current | 1-12 A (adjustable) |
| Dimensions | 250 x 826 x 630 mm |
| Net weight | **42 kg** |
| Noise at 1m | < **65 dB** |

---

## 5. ONTEK PM15SB (32 internal batteries)
**URL:** https://ontek-rus.ru/products/three-phase-ups/ibp-ontek-pm-10-80-kva/pm15sb/

Same core specs as PM10/32 with these differences:

| Parameter | PM15SB Value |
|-----------|--------------|
| Power | 15 kVA / 15 kW |
| Battery type | 12V / 9Ah (internal) |
| Battery quantity | 32 |
| Charge voltage | +/-13.65V x N (N = 16) |
| Recharge time | 4 hours to 90% capacity |
| Additional batteries | External battery modules can be connected |
| Dimensions | 250 x 826 x 630 mm |
| Net weight | **141 kg** |
| Noise at 1m | < **65 dB** |

---

## 6. ONTEK PM20SB (32 internal batteries)
**URL:** https://ontek-rus.ru/products/three-phase-ups/ibp-ontek-pm-10-80-kva/pm20sb/

Same core specs as PM10/32 with these differences:

| Parameter | PM20SB Value |
|-----------|--------------|
| Power | 20 kVA / 20 kW |
| Battery type | 12V / 9Ah (internal) |
| Battery quantity | 32 |
| Charge voltage | +/-13.65V x N (N = 16) |
| Recharge time | 4 hours to 90% capacity |
| Additional batteries | External battery modules can be connected |
| Dimensions | 250 x 826 x 630 mm |
| Net weight | **142 kg** |
| Noise at 1m | < **65 dB** |

---

## 7. ONTEK PM30SB (32x2 internal batteries)
**URL:** https://ontek-rus.ru/products/three-phase-ups/ibp-ontek-pm-10-80-kva/pm30sb/

**NOTE:** The PM30SB and PM40SB are built on a larger platform (300x1000x815 mm) and differ significantly from the 10-20 kVA models.

| Category | Parameter | Value |
|----------|-----------|-------|
| **General** | Model | PM30SB |
| | Power | 30 kVA / 30 kW |
| | Phase | 3-phase input / 3-phase output (3:3 only) |
| | Parallel operation | Up to 4 UPS (common battery group possible) |
| | Parallel board | Built-in |
| | Circuit breakers | 4 pcs: main input, output, static bypass input, mechanical bypass |
| | Breaker location | Rear of UPS |
| | Connection | Dual input: main + bypass line |
| | Cable entry | Bottom rear |
| **INPUT** | Nominal voltage | 3x 380/400/415V (3ph+N) |
| | Voltage range | 110-300V at 50% load, 176-276V at 100% load |
| | Frequency range | 40-70 Hz |
| | Power factor | >= 0.99 at 100% load |
| | THDi | < 4% at full linear load |
| **OUTPUT** | Output voltage | 3x 380/400/415V (3ph+N) |
| | Voltage regulation | +/- 1% |
| | Frequency (synced) | 46-54 Hz or 56-64 Hz |
| | Frequency (battery) | 50/60 Hz +/- 0.1 Hz |
| | Crest factor | 3:1 (max) |
| | THD | <=2% (linear load); <=5% (non-linear load) |
| | Transfer time | Zero (both battery & bypass) |
| | Waveform | Pure sine wave |
| | Overload | 100-110% 60 min, 111-125% 10 min, 126-150% 1 min; immediate >150% |
| **BYPASS** | Nominal voltage | 3x 380/400/415V (3ph+N) |
| | Voltage range | 305-457 V |
| | Frequency (synced) | 46-54 Hz or 56-64 Hz |
| | Overload | >130% 1 min (default); Continuous until breaker (optional) |
| **EFFICIENCY** | Online mode | 95.5% |
| | ECO mode | 98.5% |
| | Battery mode | 94.5% |
| **BATTERIES** | Battery type | 12V / 9Ah (internal) |
| | Battery quantity | 32 x 2 |
| | Battery service life | Standard 5 years, 10 years optional |
| | Max charge current | 1-12 A (adjustable) |
| | Charge voltage | +/-13.65V x N (N = 16) |
| | Recharge time | 9 hours to 90% capacity |
| | Additional batteries | External battery modules can be connected |
| | Charge method | 3-stage |
| | Temperature compensation | Yes |
| | Cold start | Yes |
| **DISPLAY** | Display | 5" color touch LCD |
| **MANAGEMENT** | Smart RS-232 | x1 |
| | USB | x1 |
| | Modbus card | RS485 x2, Modbus RTU |
| | Batt. temp connector | x1 (sensor included) |
| | Dry contacts | x1: 6 input signals, 4 output signals |
| | Optional | SNMP card, Environmental sensor |
| **PHYSICAL** | Dimensions (WxHxD) | **300 x 1000 x 815 mm** |
| | Net weight | **230 kg** |
| | Noise at 1m | < 65 dB |
| **ENVIRONMENT** | Operating temp & humidity | 0-40 deg C, < 95% non-condensing |
| | Altitude | 0-1500 m at full load (derate 1% per 100m above) |
| **COMPLIANCE** | Certifications | EAEU TR TS 004/2011, TR TS 020/2011, ISO 9001:2015 |
| | Warranty | 3 years (standard) or extended to 5 years |

---

## 8. ONTEK PM40SB (32x2 internal batteries)
**URL:** https://ontek-rus.ru/products/three-phase-ups/ibp-ontek-pm-10-80-kva/pm40sb/

Same frame as PM30SB (300x1000x815 mm). **Efficiency: 96% online, 99% ECO, 96% battery.**

| Category | Parameter | Value |
|----------|-----------|-------|
| **General** | Model | PM40SB |
| | Power | 40 kVA / 40 kW |
| | Phase | 3-phase input / 3-phase output (3:3 only) |
| | Parallel operation | Up to **6** UPS (common battery group possible) |
| | Parallel board | Built-in |
| | Circuit breakers | 4 pcs |
| | Breaker location | Rear of UPS |
| | Connection | Dual input |
| | Cable entry | Bottom rear |
| **INPUT** | Nominal voltage | 3x 380/400/415V (3ph+N) |
| | Voltage range | **-30% / +20%** |
| | Frequency range | 40-70 Hz |
| | Power factor | >= 0.99 at 100% load |
| | THDi | < 4% at full linear load |
| **OUTPUT** | Output voltage | 3x 380/400/415V (3ph+N) |
| | Voltage regulation | +/- 1% |
| | Frequency (synced) | 46-54 Hz or 56-64 Hz |
| | Frequency (battery) | 50/60 Hz +/- 0.1 Hz |
| | Crest factor | 3:1 (max) |
| | THD | <=2% (linear load); <=5% (non-linear load) |
| | Transfer time | Zero |
| | Waveform | Pure sine wave |
| | Overload | 100-110% 60 min, 111-125% 10 min, 126-150% 1 min; immediate >150% |
| **BYPASS** | Nominal voltage | 3x 380/400/415V (3ph+N) |
| | Voltage range | -30% / +20% (adjustable) |
| | Frequency (synced) | 46-54 Hz or 56-64 Hz |
| | Overload | >130% 1 min (default); Continuous until breaker (optional) |
| **EFFICIENCY** | Online mode | **96%** |
| | ECO mode | **99%** |
| | Battery mode | **96%** |
| **BATTERIES** | Battery type | 12V / 9Ah (internal) |
| | Battery quantity | 32 x 2 |
| | Battery service life | Standard 5 years, 10 years optional |
| | Max charge current | **1-16 A** (adjustable) |
| | Charge voltage | +/-13.65V x N (N = 16) |
| | Recharge time | 9 hours to 90% capacity |
| | Additional batteries | External battery modules can be connected |
| | Charge method | 3-stage |
| | Temperature compensation | Yes |
| | Cold start | Yes |
| **DISPLAY** | Display | 5" color touch LCD |
| **MANAGEMENT** | Smart RS-232 | x1 |
| | USB | x1 |
| | Modbus card | RS485 x2 |
| | Batt. temp connector | x1 (sensor included) |
| | Dry contacts | x1: 6 input, 4 output |
| | Optional | SNMP card, Environmental sensor |
| **PHYSICAL** | Dimensions (WxHxD) | **300 x 1000 x 815 mm** |
| | Net weight | **260 kg** |
| | Noise at 1m | < **63 dB** |
| **ENVIRONMENT** | Operating temp & humidity | 0-40 deg C, < 95% non-condensing |
| | Altitude | 0-1500 m (derate 1% per 100m above) |
| **COMPLIANCE** | Certifications | EAEU TR TS 004/2011, TR TS 020/2011, ISO 9001:2015 |
| | Warranty | 3 years (standard) or extended to 5 years |

---

---
## CATALOG LISTING PAGES (No detailed tech tables on page)

---

### 9. ONTEK PM RACK 30-60 kVA (CATALOG PAGE)
**URL:** https://ontek-rus.ru/products/three-phase-ups/ibp-ontek-pm-rack-30-60-kva/
**Type:** Catalog listing with filters, no detail tables

**Summary:**
- Format: Rack/Tower
- 10-40 kVA: size 3U
- 60 kVA: size 4U
- PF = 1
- Parallel: up to 8 UPS with common battery

**Models listed (links to individual pages):**
| Model | Phase (in/out) | Power (kVA/kW) | PF | Battery |
|-------|----------------|----------------|-----|---------|
| PM RACK 10 | 1/1, 3/1, 3/3, Multi-phase | 10/10 | 1 | External |
| PM RACK 20 | 1/1, 3/1, 3/3, Multi-phase | 20/20 | 1 | External |
| PM RACK 30 | 3/3 | 30/30 | 1 | External |
| PM RACK 40 | 3/3 | 40/40 | 1 | External |
| PM RACK 60 | 3/3 | 60/60 | 1 | External |

---

### 10. ONTEK PM TR 10-60 kVA (CATALOG PAGE)
**URL:** https://ontek-rus.ru/products/three-phase-ups/ontek-pm-tr/
**Type:** Catalog listing with filters, no detail tables

**Summary:**
- High efficiency 96.5%
- PF = 1
- Parallel up to 8 UPS
- Flexible battery config, powerful charger

**Power range:** 10, 15, 20, 30, 40, 60 kVA/kW
**Phase:** 1/1, 3/1, 3/3, Multi-phase
**Battery options:** External, Internal (various battery counts: 40, 64, 80, 96, 120, 128, 160, 200 with 5 or 10 year service life)
**Models listed:** 86 total variants including PM10SBTR, PM15SBTR, PM20SBTR, PM30SBTR, PM40SBTR, PM60TR and their sub-variants with different battery configurations

---

### 11. ONTEK TM 100-200 kVA (CATALOG PAGE)
**URL:** https://ontek-rus.ru/products/three-phase-ups/ibp-ontek-tm-100-200-kva/
**Type:** Catalog listing, no detail tables

**Summary:**
- Hot-swap power modules with dust filter
- Dual input
- Phase: 3/3, PF = 1, all external batteries

**Models:**
| Model | Power (kVA) |
|-------|-------------|
| TM80 V2 | 80 |
| TM100 | 100 |
| TM100 V2 | 100 |
| TM120 | 120 |
| TM120 V2 | 120 |
| TM160 | 160 |
| TM160 V2 | 160 |
| TM180 | 180 |
| TM180 V2 | 180 |
| TM200 | 200 |
| TM200 V2 | 200 |

---

### 12. ONTEK TM ISO 60-200 kVA (CATALOG PAGE)
**URL:** https://ontek-rus.ru/products/three-phase-ups/ibp-ontek-tm-iso-60-200-kva/
**Type:** Catalog listing, no detail tables

**Summary:**
- Built-in output isolation transformer
- Hot-swap modules, front access
- Parallel up to 4 UPS, common battery
- Phase: 3/3, PF = 1

**Models:**
| Model | Power (kVA/kW) |
|-------|----------------|
| TM ISO 60 | 60/60 |
| TM ISO 100 | 100/100 |
| TM ISO 120 | 120/120 |
| TM ISO 180 | 180/180 |
| TM ISO 200 | 200/200 |

---

### 13. ONTEK SPM Plus 20-120 kVA (CATALOG PAGE)
**URL:** https://ontek-rus.ru/products/three-phase-ups/spm-plus/
**Type:** Catalog listing, no detail tables

**Summary:**
- Modular UPS, 11/15U system cabinets
- Hot-swap modules: 10/20/30 kVA/kW, height 2U
- Phase options: 1/1, 3/1, 3/3, Multi-phase

**Models:**
| Model | Phase | Power (kVA/kW) | Module (kVA) |
|-------|-------|----------------|--------------|
| SPMPLUS20 | Multi-phase | 20/20 | 10 |
| SPMPLUS40/20 | 3/3 | 40/40 | 20 |
| SPMPLUS40 | Multi-phase | 40/40 | 10 |
| SPMPLUS60/30 | 3/3 | 60/60 | 30 |
| SPMPLUS80/20 | 3/3 | 80/80 | 20 |
| SPMPLUS120/30 | 3/3 | 120/120 | 30 |

---

### 14. ONTEK SPM 40-300 kVA (CATALOG PAGE)
**URL:** https://ontek-rus.ru/products/three-phase-ups/ibp-ontek-spm/
**Type:** Catalog listing, no detail tables

**Summary:**
- Modular UPS, interchangeable modules: power, bypass, battery
- Modules: 20kVA or 30kVA
- Cabinets: 30U or 42U
- 27 model variants across 40-300 kVA range

**Power range:** 40, 60, 80, 90, 100, 120, 140, 150, 160, 180, 200, 210, 300 kVA/kW
**All models:** 3/3 phase, PF = 1

---

### 15. ONTEK MPM 120-600 kVA (CATALOG PAGE)
**URL:** https://ontek-rus.ru/products/three-phase-ups/ibp-ontek-mpm-60-600-kva/
**Type:** Catalog listing, no detail tables

**Summary:**
- Modular UPS with hot-swap power and bypass modules
- N+1 or N+X redundancy
- 3/3 phase, PF = 1

**Models:**
| Model | Power (kVA) |
|-------|-------------|
| MPM120 | 120 |
| MPM180 | 180 |
| MPM300 | 300 |
| MPM305 | 300 (compact) |
| MPM420 | 420 |
| MPM480 | 480 |
| MPM600 | 600 |

---

### 16. ONTEK MPM Plus 200-1200 kVA (CATALOG PAGE)
**URL:** https://ontek-rus.ru/products/three-phase-ups/mpm-plus/
**Type:** Catalog listing with 2 sub-categories

**Sub-categories:**
1. **MPM Plus 200-600 kVA** with 50 kVA modules (3U hot-swap)
2. **MPM Plus 600-1200 kVA** with 100 kVA modules (3U hot-swap)

---

### 17. ONTEK iDS 10-200 kVA (CATALOG PAGE)
**URL:** https://ontek-rus.ru/products/three-phase-ups/ids/
**Type:** Catalog listing, no detail tables

**Summary:**
- Built-in isolation transformer
- Models designated as iDS XX-3Y (XX = power kVA, Y = phase: 1=1ph out, 3=3ph out)

**Models (19 total):**
| Model | Phase | kVA/kW | PF |
|-------|-------|--------|-----|
| iDS 10-31 | 3/1 | 10/8 | 0.8 |
| iDS 10-33 | 3/3 | 10/9 | 0.9 |
| iDS 15-31 | 3/1 | 15/12 | 0.8 |
| iDS 15-33 | 3/3 | 15/13.5 | 0.9 |
| iDS 20-31 | 3/1 | 20/16 | 0.8 |
| iDS 20-33 | 3/3 | 20/18 | 0.9 |
| iDS 30-31 | 3/1 | 30/24 | 0.8 |
| iDS 30-33 | 3/3 | 30/27 | 0.9 |
| iDS 40-31 | 3/1 | 40/32 | 0.8 |
| iDS 40-33 | 3/3 | 40/36 | 0.9 |
| iDS 60-31 | 3/1 | 60/48 | 0.8 |
| iDS 60-33 | 3/3 | 60/54 | 0.9 |
| iDS 80-31 | 3/1 | 80/64 | 0.8 |
| iDS 80-33 | 3/3 | 80/72 | 0.9 |
| iDS 100-31 | 3/1 | 100/80 | 0.8 |
| iDS 100-33 | 3/3 | 100/90 | 0.9 |
| iDS 120-33 | 3/3 | 120/108 | 0.9 |
| iDS 160-33 | 3/3 | 160/144 | 0.9 |
| iDS 200-33 | 3/3 | 200/180 | 0.9 |

---

### 18. ONTEK SM RT 1-3 kVA (CATALOG PAGE)
**URL:** https://ontek-rus.ru/products/single-phase-ups/ibp-ontek-sm-rt-1-3-kva/
**Type:** Catalog listing, no detail tables

**Summary:**
- Online double conversion
- PF = 1
- Hot-swap batteries
- ECO mode
- Phase: 1/1

**Models (20 total) including V2 versions, variants with internal/external batteries:**
| Power Range | Models |
|-------------|--------|
| 1 kVA/1 kW | SMRT 1, SMRT 1 V2, SMRT1SBUL10, SMRT1SBUL10 V2, SMRT 1 /wo, SMRT 1 /wo V2 |
| 1.5 kVA/1.5 kW | SMRT 1,5, SMRT 1,5 /wo |
| 2 kVA/2 kW | SMRT 2, SMRT 2 V2, SMRT2SBUL10, SMRT2SBUL10 V2, SMRT 2 /wo, SMRT 2 /wo V2 |
| 3 kVA/3 kW | SMRT3, SMRT3 V2, SMRT3SBUL10, SMRT3SBUL10 V2, SMRT 3 /wo, SMRT 3 /wo V2 |

---

### 19. ONTEK SMX RT 1-3 kVA (CATALOG PAGE)
**URL:** https://ontek-rus.ru/products/single-phase-ups/ibp-ontek-smx-rt-1-3-kva/
**Type:** Catalog listing, no detail tables

**Summary:**
- Online double conversion
- PF = 1
- 3-stage charging
- All models: 1/1 phase, internal batteries

**Models (6 total):**
| Model | Power (kVA/kW) | Battery Life |
|-------|----------------|--------------|
| SMXRT 1 | 1/1 | 5 years |
| SMXRT 1/10 | 1/1 | 10 years |
| SMXRT 2 | 2/2 | 5 years |
| SMXRT 2/10 | 2/2 | 10 years |
| SMXRT 3 | 3/3 | 5 years |
| SMXRT 3/10 | 3/3 | 10 years |

---

### 20. ONTEK SM RM 1-3 kVA (CATALOG PAGE)
**URL:** https://ontek-rus.ru/products/single-phase-ups/ibp-ontek-sm-rm-1-3-kva/
**Type:** Catalog listing, no detail tables

**Summary:**
- Online double conversion
- PF = 0.9
- Rack-mount format
- Phase: 1/1

**Models (3 total):**
| Model | Power (kVA/kW) | PF |
|-------|----------------|-----|
| SMRM 1 | 1/0.9 | 0.9 |
| SMRM 2 | 2/1.8 | 0.9 |
| SMRM 3 | 3/2.7 | 0.9 |

---

### 21. ONTEK SM RT 6-10 kVA (CATALOG PAGE)
**URL:** https://ontek-rus.ru/products/single-phase-ups/ibp-ontek-sm-rt-6-10-kva/
**Type:** Catalog listing, no detail tables

**Summary:**
- Online double conversion
- PF = 1
- SNMP/USB/RS-232
- EPO function
- Phase: 1/1

**Models (6 total):**
| Model | Power (kVA/kW) | Battery |
|-------|----------------|---------|
| SM RT 6 | 6/6 | External |
| SM RT 6 (SB) | 6/6 | Internal |
| SM RT 6 V2 | 6/6 | External |
| SM RT 10 | 10/10 | External |
| SM RT 10 (SB) | 10/10 | Internal |
| SM RT 10 V2 | 10/10 | External |

---

### 22. ONTEK OLIO LiFePO4 (CATALOG PAGE)
**URL:** https://ontek-rus.ru/products/single-phase-ups/ibp-ontek-olio/
**Type:** Catalog listing, no detail tables

**Summary:**
- Lithium-ion (LiFePO4)
- 2x less space, 3x longer life vs VRLA
- Modular design
- Rack/Tower convertible
- BMS system
- Phase: 1/1, PF = 1

**Models (3 basic):**
| Model | Power (kVA/kW) |
|-------|----------------|
| OLIO1000 | 1/1 |
| OLIO2000 | 2/2 |
| OLIO3000 | 3/3 |

(Additional sub-variants available with different battery configurations)

---

### 23. ONTEK 3S Line-Interactive (CATALOG PAGE)
**URL:** https://ontek-rus.ru/products/single-phase-ups/3s/
**Type:** Catalog listing, no detail tables

**Summary:**
- Line-interactive topology
- LCD display, USB, RS-232
- Automatic restart
- Phase: 1/1

**Models (6 total):**
| Model | Power (kVA/kW) |
|-------|----------------|
| 3S 550 | 0.55/0.3 |
| 3S 550-SC | 0.55/0.3 |
| 3S 650 | 0.65/0.36 |
| 3S 650-SC | 0.65/0.36 |
| 3S 850 | 0.85/0.48 |
| 3S 850-SC | 0.85/0.48 |

---

### 24. Downloads Center (CATALOG PAGE)
**URL:** https://ontek-rus.ru/support/downloads/
**Type:** Download center with search/filter - document repository

**Available document types per product series:**
- Brochures, Passports (datasheets), Certificates (EAC, ISO 9001, seismic), User manuals
- SNMP/web-card documentation
- Modbus documentation
- CAD drawings

**Key files referenced across PM series pages:**
- Паспорт ONTEK PM (968 KB) - ONTEK PM datasheet/passport
- Сертификат сейсмостойкости (737 KB) - Seismic certificate (9 points MSK-64)
- Сертификат соответствия ЕАС (1.27 MB) - EAC certificate
- Сертификат ISO-9001 (468 KB)
- Руководство пользователя ONTEK PM 10-80 кВА (3.54 MB) - User manual

---

## PM SERIES COMPARISON SUMMARY TABLE

| Model | Power (kVA/kW) | Phase | Weight (kg) | Dims WxHxD (mm) | Noise (dB) | Battery | Bat Qty | Efficiency Online/ECO/Bat | Parallel |
|-------|----------------|-------|-------------|------------------|------------|---------|---------|---------------------------|----------|
| PM10/32 | 10/10 | Multi | 40 | 250x826x630 | <60 | Ext 32-40 | 32-40 | 95.5/98.5/94.5% | Up to 4 |
| PM10SB/20 | 10/10 | Multi | 126 | 250x826x630 | <60 | Int 12V/9Ah | 20 | 95.5/98.5/94.5% | Up to 4 |
| PM10SB/32 | 10/10 | Multi | 138 | 250x826x630 | <60 | Int 12V/9Ah | 32 | 95.5/98.5/94.5% | Up to 4 |
| PM15 | 15/15 | Multi | 42 | 250x826x630 | <65 | Ext 32-40 | 32-40 | 95.5/98.5/94.5% | Up to 4 |
| PM15SB | 15/15 | Multi | 141 | 250x826x630 | <65 | Int 12V/9Ah | 32 | 95.5/98.5/94.5% | Up to 4 |
| PM20SB | 20/20 | Multi | 142 | 250x826x630 | <65 | Int 12V/9Ah | 32 | 95.5/98.5/94.5% | Up to 4 |
| PM30SB | 30/30 | 3:3 | 230 | 300x1000x815 | <65 | Int 12V/9Ah | 32x2 | 95.5/98.5/94.5% | Up to 4 |
| PM40SB | 40/40 | 3:3 | 260 | 300x1000x815 | <63 | Int 12V/9Ah | 32x2 | 96/99/96% | Up to 6 |

---

## COMMON SPECIFICATIONS (All PM Series)

| Parameter | 10-20 kVA Models | 30-40 kVA Models |
|-----------|-----------------|-------------------|
| Input nominal voltage | 1x 220/230/240V or 3x 380/400/415V | 3x 380/400/415V |
| Input voltage range (100% load) | 176-276V | 176-276V (30SB), -30%/+20% (40SB) |
| Input frequency | 46-54 / 56-64 Hz (10-20), 40-70 Hz (30-40) | 40-70 Hz |
| Output voltage | Same as input | 3x 380/400/415V |
| Voltage regulation | +/- 1% | +/- 1% |
| Crest factor | 3:1 | 3:1 |
| THD (linear) | <=2% | <=2% |
| THD (non-linear) | <=5% | <=5% |
| Transfer time | Zero | Zero |
| Waveform (battery) | Pure sine wave | Pure sine wave |
| Display | 5" color touch LCD | 5" color touch LCD |
| Interfaces | RS-232, USB, Modbus, dry contacts | RS-232, USB, Modbus, dry contacts |
| Operating temp | 0-40 deg C | 0-40 deg C |
| Humidity | <95% non-condensing | <95% non-condensing |
| Altitude | 0-1500m (1%/100m derate) | 0-1500m (1%/100m derate) |
| Certifications | EAEU TR TS, ISO 9001:2015 | EAEU TR TS, ISO 9001:2015 |
| Warranty | 3 years (ext. to 5) | 3 years (ext. to 5) |
