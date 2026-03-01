<!--
  PAPER CONTEXT FILE  —  for use with Claude
  ─────────────────────────────────────────────
  How to use:
  1. Attach this file and the PNG images to a Claude conversation.
  2. Say: "Using the context file below, explain [topic] as Feynman
     would — starting from [basic concept] and building up step by step."
  3. The 'Referenced in paper' sentences are the authors' own words
     about each figure — the most reliable guide to its meaning.
-->

# Paper Context: DLVBMCHBC — DC-Link_Voltage_Balancing_Modulation_for_Cascaded_H-Bridge_Converters.pdf

*Generated: 2026-03-01  |  Figures: 14  |  Pages: 9*

---

## Paper Overview

*(Auto-extracted from the first pages — edit for accuracy)*

Received June 27, 2021, accepted July 8, 2021, date of publication July 20, 2021, date of current version July 28, 2021.

DC-Link Voltage Balancing Modulation for Cascaded H-Bridge Converters

YOUNGJONG KO 1, (Member, IEEE), ANATOLII TCAI 2, (Student Member, IEEE), AND MARCO LISERRE 2, (Fellow, IEEE) 1Department of Electrical Engineering and Industry 4.0 Convergence Bionics Engineering, Pukyong National University, Busan 48513, South Korea 2Chair of Power Electronics, Christian-Albrechts-University of Kiel, 24143 Kiel, Germany

Corresponding author: Youngjong Ko (yjko@pknu.ac.kr)

This work was supported by a Research Grant of Pukyong National University (2020).

ABSTRACT Cascaded H-Bridge (CHB) converters have been widely employed in various applications, providing the advantages of modularity and multilevel voltage output. However, technically the CHB converters require isolated DC-link buses, which need to be regulated individually. In this context, a control scheme for the CHB converters features the voltage balancing algorithm. The voltage balancing control is typically performed by PI controller, where its control capability is limited by linear modulation region. In this work, the modulation based voltage balancing algorithm is proposed, which extends the balancing control capability and improves the dynamic performance. The proposed method is theoretically analyzed and validated through the simulation and experimental results.

INDEX TERMS Multilevel converter, Cascaded-H bridge converter, DC-link voltage balancing, modulation.

I. INTRODUCTION Cascaded H-Bridge (CHB) converters feature modularity, multilevel voltage output, and low dv/dt, which offers merits to high power applications [1]–[3]. Fig. 1 shows a general structure of grid-connected CHB converter, which consists of the n cells and n isolated DC-link buses. Furthermore, the loading power of each cell is presented, where the remark- able point is that each cell is able to transfer different amount of power. In some applications, either the unbalanced loading power is unavoidable or the loading power of each cell is controlled to be unbalanced on purpose. The multi-string photovoltaic systems, where each string is connected to the respective DC bus, is one of the representative examples [4]–[7]. In such systems, a mismatch in the operating conditions inherently results in the unbalanced power generation among the strings. Moreover, the generated power of individual string is typi- cally controlled by a respective maximum power point track- ing algorithm in order to maximize the harvested power. Therefore, the power imbalance among the cells shall be further elevated. As another example, considering that indi- vidual cell has different Remaining Useful Lifetime (RUL),

The associate editor coordinating the review of this manuscript and

approving it for publication was Chen Chen .

FIGURE 1. Grid-connected CHB converter with unbalanced loading power, P1H ̸= P2H ̸= P3H .

the power routing strategy was proposed in [8] and [9], which aims at unequally redistributing total power among the cells. The loading power …

---

## Figure Index

| Figure | Page | File | Section |
|--------|------|------|---------|
| Fig. 1 | 1 | `DLVBMCHBC_Fig1_page01.png` | YOUNGJONG KO |
| Fig. 2 | 2 | `DLVBMCHBC_Fig2_page02.png` | Y. Ko et al.: DC-Link Voltage Balancing Modulation for CHB Converters |
| Fig. 3 | 2 | `DLVBMCHBC_Fig3_page02.png` | Y. Ko et al.: DC-Link Voltage Balancing Modulation for CHB Converters |
| Fig. 4 | 3 | `DLVBMCHBC_Fig4_page03.png` | B. IMPLEMENTATION |
| Fig. 5 | 3 | `DLVBMCHBC_Fig5_page03.png` | B. IMPLEMENTATION |
| Fig. 6 | 4 | `DLVBMCHBC_Fig6_page04.png` | Y. Ko et al.: DC-Link Voltage Balancing Modulation for CHB Converters |
| Fig. 7 | 4 | `DLVBMCHBC_Fig7_page04.png` | Y. Ko et al.: DC-Link Voltage Balancing Modulation for CHB Converters |
| Fig. 8 | 4 | `DLVBMCHBC_Fig8_page04.png` | Y. Ko et al.: DC-Link Voltage Balancing Modulation for CHB Converters |
| Fig. 9 | 4 | `DLVBMCHBC_Fig9_page04.png` | Y. Ko et al.: DC-Link Voltage Balancing Modulation for CHB Converters |
| Fig. 10 | 5 | `DLVBMCHBC_Fig10_page05.png` | Y. Ko et al.: DC-Link Voltage Balancing Modulation for CHB Converters |
| Fig. 11 | 6 | `DLVBMCHBC_Fig11_page06.png` | IV. SIMULATION VALIDATION |
| Fig. 12 | 6 | `DLVBMCHBC_Fig12_page06.png` | Y. Ko et al.: DC-Link Voltage Balancing Modulation for CHB Converters |
| Fig. 13 | 7 | `DLVBMCHBC_Fig13_page07.png` | Y. Ko et al.: DC-Link Voltage Balancing Modulation for CHB Converters |
| Fig. 14 | 8 | `DLVBMCHBC_Fig14_page08.png` | Y. Ko et al.: DC-Link Voltage Balancing Modulation for CHB Converters |

---

## Figure 1 — Page 1

**File:** `DLVBMCHBC_Fig1_page01.png`  
**Dimensions:** 715 x 507 px  
**Section:** YOUNGJONG KO

**Caption:**
> FIGURE 1. Grid-connected CHB converter with unbalanced loading power, P1H ̸= P2H ̸= P3H .

**Referenced in paper:** *(none found — may be a scanned PDF)*

**Feynman entry point:** *(Claude: fill in)*
> What is the simplest real-world analogy for what this figure shows?
> What single concept does it primarily illustrate,
> and what prerequisite knowledge does a reader need?

---

## Figure 2 — Page 2

**File:** `DLVBMCHBC_Fig2_page02.png`  
**Dimensions:** 688 x 305 px  
**Section:** Y. Ko et al.: DC-Link Voltage Balancing Modulation for CHB Converters

**Caption:**
> FIGURE 2. Typical control scheme for grid-connected CHB converter.

**Referenced in paper:** *(none found — may be a scanned PDF)*

**Feynman entry point:** *(Claude: fill in)*
> What is the simplest real-world analogy for what this figure shows?
> What single concept does it primarily illustrate,
> and what prerequisite knowledge does a reader need?

---

## Figure 3 — Page 2

**File:** `DLVBMCHBC_Fig3_page02.png`  
**Dimensions:** 724 x 349 px  
**Section:** Y. Ko et al.: DC-Link Voltage Balancing Modulation for CHB Converters

**Caption:**
> FIGURE 3. Conventional PI loop-based voltage balancing algorithm [19].

**Referenced in paper:** *(none found — may be a scanned PDF)*

**Feynman entry point:** *(Claude: fill in)*
> What is the simplest real-world analogy for what this figure shows?
> What single concept does it primarily illustrate,
> and what prerequisite knowledge does a reader need?

---

## Figure 4 — Page 3

**File:** `DLVBMCHBC_Fig4_page03.png`  
**Dimensions:** 625 x 501 px  
**Section:** B. IMPLEMENTATION

**Caption:**
> FIGURE 4. Principle of the proposed method when Vdc,1H > Vdc,1H > . . . > Vdc,(n−1)H > Vdc,nH as an example.

**Referenced in paper:** *(none found — may be a scanned PDF)*

**Feynman entry point:** *(Claude: fill in)*
> What is the simplest real-world analogy for what this figure shows?
> What single concept does it primarily illustrate,
> and what prerequisite knowledge does a reader need?

---

## Figure 5 — Page 3

**File:** `DLVBMCHBC_Fig5_page03.png`  
**Dimensions:** 685 x 418 px  
**Section:** B. IMPLEMENTATION

**Caption:**
> FIGURE 5. A case study with two cells and tbal of 5 ms; modulation signal for (a) cell 1 and (b) cell 2 (considering vg · ig < 0).

**Referenced in paper:** *(none found — may be a scanned PDF)*

**Feynman entry point:** *(Claude: fill in)*
> What is the simplest real-world analogy for what this figure shows?
> What single concept does it primarily illustrate,
> and what prerequisite knowledge does a reader need?

---

## Figure 6 — Page 4

**File:** `DLVBMCHBC_Fig6_page04.png`  
**Dimensions:** 691 x 933 px  
**Section:** Y. Ko et al.: DC-Link Voltage Balancing Modulation for CHB Converters

**Caption:**
> FIGURE 6. Five cases occurred in four cells (operation mode without bracket: vg · ig < 0 and with bracket: vg · ig > 0).

**Referenced in paper:** *(none found — may be a scanned PDF)*

**Feynman entry point:** *(Claude: fill in)*
> What is the simplest real-world analogy for what this figure shows?
> What single concept does it primarily illustrate,
> and what prerequisite knowledge does a reader need?

---

## Figure 7 — Page 4

**File:** `DLVBMCHBC_Fig7_page04.png`  
**Dimensions:** 693 x 244 px  
**Section:** Y. Ko et al.: DC-Link Voltage Balancing Modulation for CHB Converters

**Caption:**
> FIGURE 7. Clamped modulation signal with varied clamping angle ϕ.

**Referenced in paper:** *(none found — may be a scanned PDF)*

**Feynman entry point:** *(Claude: fill in)*
> What is the simplest real-world analogy for what this figure shows?
> What single concept does it primarily illustrate,
> and what prerequisite knowledge does a reader need?

---

## Figure 8 — Page 4

**File:** `DLVBMCHBC_Fig8_page04.png`  
**Dimensions:** 733 x 425 px  
**Section:** Y. Ko et al.: DC-Link Voltage Balancing Modulation for CHB Converters

**Caption:**
> FIGURE 8. Loading power as a function of the nominal modulation index and the clamping angle; (a) clamped mode and (b) non-clamped mode.

**Referenced in paper:** *(none found — may be a scanned PDF)*

**Feynman entry point:** *(Claude: fill in)*
> What is the simplest real-world analogy for what this figure shows?
> What single concept does it primarily illustrate,
> and what prerequisite knowledge does a reader need?

---

## Figure 9 — Page 4

**File:** `DLVBMCHBC_Fig9_page04.png`  
**Dimensions:** 703 x 428 px  
**Section:** Y. Ko et al.: DC-Link Voltage Balancing Modulation for CHB Converters

**Caption:**
> FIGURE 9. Comparison of maximum loading power with conventional method.

**Referenced in paper:** *(none found — may be a scanned PDF)*

**Feynman entry point:** *(Claude: fill in)*
> What is the simplest real-world analogy for what this figure shows?
> What single concept does it primarily illustrate,
> and what prerequisite knowledge does a reader need?

---

## Figure 10 — Page 5

**File:** `DLVBMCHBC_Fig10_page05.png`  
**Dimensions:** 1578 x 1365 px  
**Section:** Y. Ko et al.: DC-Link Voltage Balancing Modulation for CHB Converters

**Caption:**
> FIGURE 10. Control performance of (a) conventional method and (b) proposed method with −1 power factor, and (c) proposed method with −0.8 power factor (Pmax = 1.25 and Pmin = 0.75 at 0.5 sec).

**Referenced in paper:** *(none found — may be a scanned PDF)*

**Feynman entry point:** *(Claude: fill in)*
> What is the simplest real-world analogy for what this figure shows?
> What single concept does it primarily illustrate,
> and what prerequisite knowledge does a reader need?

---

## Figure 11 — Page 6

**File:** `DLVBMCHBC_Fig11_page06.png`  
**Dimensions:** 736 x 911 px  
**Section:** IV. SIMULATION VALIDATION

**Caption:**
> FIGURE 11. Maximum control performance with (a) conventional method and (b) proposed method (power factor = −1, Pmax = 1.62 and Pmin = 0.38).

**Referenced in paper:** *(none found — may be a scanned PDF)*

**Feynman entry point:** *(Claude: fill in)*
> What is the simplest real-world analogy for what this figure shows?
> What single concept does it primarily illustrate,
> and what prerequisite knowledge does a reader need?

---

## Figure 12 — Page 6

**File:** `DLVBMCHBC_Fig12_page06.png`  
**Dimensions:** 697 x 378 px  
**Section:** Y. Ko et al.: DC-Link Voltage Balancing Modulation for CHB Converters

**Caption:**
> FIGURE 12. Developed prototype consisting of 3 cells.

**Referenced in paper:** *(none found — may be a scanned PDF)*

**Feynman entry point:** *(Claude: fill in)*
> What is the simplest real-world analogy for what this figure shows?
> What single concept does it primarily illustrate,
> and what prerequisite knowledge does a reader need?

---

## Figure 13 — Page 7

**File:** `DLVBMCHBC_Fig13_page07.png`  
**Dimensions:** 1578 x 640 px  
**Section:** Y. Ko et al.: DC-Link Voltage Balancing Modulation for CHB Converters

**Caption:**
> FIGURE 13. Control performance in steady state: (a) Pmax = Pmin = 1.0, (b) Pmax = 1.2 and Pmin = 0.8, (c) Pmax = 1.4 and Pmin = 0.6 (top: conventional, bottom: proposed.

**Referenced in paper:** *(none found — may be a scanned PDF)*

**Feynman entry point:** *(Claude: fill in)*
> What is the simplest real-world analogy for what this figure shows?
> What single concept does it primarily illustrate,
> and what prerequisite knowledge does a reader need?

---

## Figure 14 — Page 8

**File:** `DLVBMCHBC_Fig14_page08.png`  
**Dimensions:** 709 x 752 px  
**Section:** Y. Ko et al.: DC-Link Voltage Balancing Modulation for CHB Converters

**Caption:**
> FIGURE 14. Dynamic response with (a) conventional method and (b) proposed method.

**Referenced in paper:** *(none found — may be a scanned PDF)*

**Feynman entry point:** *(Claude: fill in)*
> What is the simplest real-world analogy for what this figure shows?
> What single concept does it primarily illustrate,
> and what prerequisite knowledge does a reader need?

---
