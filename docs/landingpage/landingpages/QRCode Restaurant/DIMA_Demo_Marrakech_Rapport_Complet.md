# 🚀 DIMA Solutions AI Tech — Rapport Scénario de Démo Complet
## Cible : Riad / Restaurant Marrakech — Conversion en 45 minutes
### Basé sur : Plan Complet QR Code Dynamique v1.0

---

## 1. CONTEXTE STRATÉGIQUE & CIBLE

### Profil cible — Marrakech

| Critère | Détail |
|---|---|
| **Type** | Hôtels 3-4★ Guéliz, Ryads médina, Restaurants touristiques |
| **Digitalisation** | En cours — site web basique, WhatsApp Business, pas de système intégré |
| **Budget** | Disponible (marges hôtelières 40-60%), décision rapide possible |
| **Douleur #1** | Barrière linguistique touristes étrangers |
| **Douleur #2** | Cartes papier coûteuses (300-800 MAD/mois) à réimprimer |
| **Douleur #3** | Perte de commandes / erreurs cuisine / plats rupture non communiqués |
| **Exemples** | Hôtel & Ryad Art Place, Kenzi Menara Palace, La Maison Arabe |

### Zones de prospection prioritaires — Marrakech

- **Médina** : Derb Dabachi, Sidi Bouamar → riads traditionnels, cible émotionnelle forte
  - Horaire idéal : 15h-17h (entre déjeuner et dîner)
  - Accès : petit taxi depuis Jemaa el-Fna (10-15 MAD)
- **Guéliz** : Avenue Mohammed V, Rue de la Liberté → hôtels modernes, budget plus large
  - Prendre RDV à l'avance via LinkedIn/Instagram
- **Palmeraie** : Resorts et hôtels de luxe → cibler directeur F&B, pas le propriétaire

### Interlocuteurs à cibler (ordre de priorité)

1. **Directeur Général / Propriétaire** → décision finale, sensible au ROI global
2. **Responsable F&B** → pain point quotidien, devient champion interne naturel
3. **Directeur Marketing** → sensible à l'image de marque et expérience client premium

---

## 2. PRÉPARATION HARDWARE — CHECKLIST COMPLÈTE (J-2 à J-1)

### 2.1 Appareils & Connectivité

- [ ] **Terminal Android** Zebra TC21 ou Honeywell CT45
  - Préchargé : app de scan démo + dashboard cuisine + app impression
  - Batterie 100% + powerbank de secours
- [ ] **2 Tablettes** iPad ou Samsung Tab A8
  - Tablette 1 : interface client (menu demo)
  - Tablette 2 : dashboard admin (commandes temps réel)
- [ ] **Smartphone commercial** : SIM data active 4G/5G (test scan QR)
- [ ] **Clé USB modem 4G** ou hotspot dédié — NE JAMAIS dépendre du WiFi hôtel
- [ ] **2× Powerbank 20 000 mAh** + câbles USB-C / Lightning / Micro-USB

### 2.2 Imprimante Thermique Portable

**Modèle recommandé** : Zebra ZQ320 Plus ou iDPRT SP410 BT

| Critère | Spécification |
|---|---|
| Connectivité | Bluetooth 5.0 + USB-C charge |
| Papier | Rouleaux 58mm (tickets) + 80mm (étiquettes QR) |
| Autonomie | ≥ 500 impressions/charge |
| Poids | < 500g (portable) |

**Checklist avant démo :**
- [ ] Batterie 100%
- [ ] Rouleau 58mm plein (test impression à froid la veille)
- [ ] Appairage Bluetooth vérifié avec chaque tablette et terminal
- [ ] Driver/app installé sur tous les appareils
- [ ] 3 rouleaux de rechange dans le sac

---

## 3. FORMATS D'IMPRESSION QR CODE — SPÉCIFICATIONS DÉTAILLÉES

### Format A — Étiquette Table (format principal démo)

```
┌──────────────────────────────┐
│     [LOGO HÔTEL / DIMA]      │  ← Logo personnalisé par établissement
│                              │
│         [QR CODE]            │  ← 6×6 cm minimum (scannable à 60cm)
│                              │
│        TABLE N° 12           │  ← Numéro lisible à 1m
│   Scannez pour commander     │
│    امسح للطلب  |  Scan here  │
└──────────────────────────────┘
Format physique : 10×10 cm
Matière : PVC rigide 3mm avec base aimantée ou pied transparent
Finition : Plastifiée mat anti-reflet (crucial pour photos HD scan)
Token URL : menu.dima-solutions.ma/demo/a1b2c3d4?table=12&lang=auto
```

### Format B — Étiquette Chambre (Room Service)

```
┌───────────────────────────────┐
│      ROOM SERVICE 24/7        │
│       خدمة الغرف              │
│                               │
│          [QR CODE]            │  ← Même token + param ?room=305
│                               │
│         CHAMBRE 305           │
│   Commandez sans décrocher    │
└───────────────────────────────┘
Format : 8×12 cm
Matière : Carton épais 350g ou PVC souple
Position : Bureau de la chambre ou porte intérieure
```

### Format C — Carte de Visite NFC + QR (commercial)

```
┌──────────────────────────────────┐
│  🚀 DIMA Solutions AI Tech       │
│                                  │
│  [QR CODE 25×25mm]  [NFC puce]   │
│                                  │
│  [Nom Commercial]                │
│  +212 6XX XX XX XX               │
│  demo.dima-solutions.ma          │
└──────────────────────────────────┘
Format : 85×55 mm (standard CB)
QR → demo.dima-solutions.ma ou Calendly
NFC → calendly.com/dimasolutions/demo
Impression : Vernis sélectif recto, mat verso
```

### Format D — Ticket Thermique 58mm (commande cuisine)

```
================================
    🚀 DIMA Solutions AI Tech
         [NOM DU RIAD]
================================
Table : 12  | 06/06/2026 12:34
Ref Cmd : #CMD-20260606-0047
--------------------------------
1× Tajine d'agneau aux pruneaux  95 MAD
2× Salade marocaine              110 MAD
1× Thé à la menthe               20 MAD
     Eau minérale ×2             30 MAD
--------------------------------
SOUS-TOTAL                      255 MAD
TVA 10%                          25 MAD
TOTAL                           280 MAD
--------------------------------
Paiement : CMI ✅ / Cash ⬜
Allergènes : 🥜 Noix présentes
================================
⭐ Donnez-nous votre avis :
[QR MINI] g.page/riad-xxxxxx/review
================================
Merci & à bientôt ! شكراً جزيلاً
================================
```

### 5 QR Codes physiques à préparer pour la démo

| N° | Étiquette | Paramètre URL | Matière | Priorité |
|---|---|---|---|---|
| 1 | **Table 12** (démo principale) | `?table=12&lang=auto` | PVC rigide | ⭐⭐⭐ |
| 2 | **Table 8** (backup si table 12 prise) | `?table=8&lang=auto` | PVC rigide | ⭐⭐ |
| 3 | **Chambre 305** (room service) | `?room=305&lang=auto` | Carton 350g | ⭐⭐ |
| 4 | **Bar/Lounge** | `?zone=bar&lang=auto` | PVC rigide | ⭐ |
| 5 | **Démo commerciale** (carte de visite) | `?mode=demo&lang=fr` | PVC 85×55mm | ⭐⭐⭐ |

**Token de démo universel** : `a1b2c3d4-e5f6-7890-abcd-ef1234567890`
**URL base** : `https://menu.dima-solutions.ma/demo/{token}`

---

## 4. SÉQUENCE DE DÉMO — SCRIPT COMPLET 45 MIN CHRONO

### PHASE 1 — Accroche & Ancrage (0-10 min)

**[00:00] La poignée de main psychologique**
> Arriver 15 min avant. Repérer la salle. Poser discrètement le QR code table 12.
> "Salam alaykom [Prénom], merci de nous recevoir. Avant de commencer, pouvez-vous me décrire votre plus grande difficulté avec la gestion des menus et commandes ?"

*Laisser parler. Prendre note. Acquiescer. NE PAS couper.*

**[05:00] Le chiffre qui ancre**
> "Nos clients à Casablanca ont réduit de **73%** le temps de prise de commande et augmenté leur panier moyen de **22%** en 3 mois. Je vais vous montrer exactement pourquoi — et c'est vous qui allez le faire vous-même."

**[07:00] La feuille de route de la démo**
> "Aujourd'hui, je vous propose 3 étapes :
> 1. Je scanne ce QR comme un client — vous voyez ce que voient vos clients
> 2. Vous voyez la commande arriver en cuisine en temps réel
> 3. On imprime un ticket ensemble
> Ça vous va ?"

---

### PHASE 2 — Démo Immersive (10-30 min)

**[10:00] Le QR sort de votre poche**
> Sortez le QR code plastique rigide. Posez-le sur la table entre vous.
> "Imaginez : un couple espagnol s'assoit à cette table. Ils sortent leur iPhone..."
> *Tendez le QR au prospect — lui faire scanner lui-même.*

**[11:00] La détection de langue — premier wow**
> Le menu s'ouvre en ESPAGNOL automatiquement.
> "Vous voyez ? Aucune action de votre part. Détection automatique de la langue du téléphone."

**[12:00] La visite guidée**
> "Regardez :
> • Photos HD des plats
> • Prix en MAD ET en EUR simultanément
> • Allergènes avec icônes claires 🥜🥛🌾
> • Tajine d'agneau : marqué 'Rupture' — grisé, impossible à commander
>   Zéro frustration client. Zéro excuse à donner."

**[14:00] La commande en direct**
> Ajoutez 2 plats. Validez.
> "Regardez sur ce dashboard..." ← retournez la tablette admin.
> La commande #47 — Table 12 apparaît en temps réel.
> "Plus de bon papier. Plus de malentendu. L'heure et la table sont automatiques."

**[17:00] Le wow effect : changement en live**
> "Vos concurrents réimpriment leur carte. Vous..." → changez un prix sur le dashboard.
> "Voilà — mis à jour sur TOUS les QR codes de l'hôtel. En 3 secondes. Sans réimprimer."

**[22:00] L'impression thermique — preuve physique**
> Connectez l'imprimante Bluetooth. Imprimez.
> "Le ticket sort en 2 secondes. Sans internet." → Tendez le ticket au prospect.
> "Idéal pour les riads en vieille médina avec connexion faible."

**[26:00] L'avis Google — cercle vertueux**
> "Et après le repas..." → scannez le QR Avis.
> → La page Google Maps du riad s'ouvre avec 5 étoiles pré-sélectionnées.
> "Vos clients satisfaits deviennent vos meilleurs ambassadeurs."

**[28:00] Le QR cadeau**
> Imprimez un QR code personnalisé avec le nom du riad.
> "Gardez-le comme souvenir de notre rencontre. Ce QR pointe vers votre futur menu digital."

---

### PHASE 3 — Closing & Offre (30-45 min)

**[30:00] La fiche tarifaire — l'offre Package "Riad Digital"**
```
🎁 OFFRE LANCEMENT MARRAKECH
Package "Riad Digital"
• Menu QR multilingue (7 langues)
• Dashboard cuisine + notifications KDS
• Paiement CMI intégré
• 10 QR codes physiques inclus
• Formation équipe (1h sur site)
• Support WhatsApp FR/AR 7j/7
• Analytics avancées
──────────────────────────
Setup initial    : 3 500 MAD
Abonnement       : 2 490 MAD/mois
🎁 Imprimante thermique OFFERTE
   si signature avant [date + 7 jours]
```

**[33:00] L'urgence avec exclusivité**
> "Cette offre est réservée aux 10 premiers riads de Marrakech. L'imprimante thermique — normalement 2 500 MAD — est offerte si on signe avant le [date]. Qu'en pensez-vous ?"

**[38:00] La question à choix forcé**
> "Est-ce que vous voulez commencer avec la salle du restaurant, ou directement avec le room service également ?"
> *(Les deux options impliquent la signature)*

**[40:00] Si hésitation : l'essai sans risque**
> "Je peux vous laisser le QR de démo installé sur votre table 12 pendant 48h. Vos vrais clients pourront tester. On se rappelle jeudi pour votre retour ?"

**[43:00] La signature**
> Contrat simplifié 1 page bilingue FR/AR
> Signature électronique via tablette
> Envoi immédiat facture proforma sur WhatsApp

**[45:00] La clôture culturelle**
> "Merci [Prénom] ! L'équipe technique vous contacte demain. Baraka Allah fik!"

---

## 5. GESTION DES OBJECTIONS — SCRIPT BILINGUE

| Objection | Réponse FR | Réponse AR |
|---|---|---|
| **"C'est trop cher"** | "Réimpression = 300-800 MAD/mois. Rotation table +25%. ROI en 6 semaines." | "إعادة الطباعة 300-800 درهم شهرياً. العائد في 6 أسابيع." |
| **"Mes clients préfèrent le papier"** | "95% des touristes scannent déjà. On garde 2 menus papier en réserve." | "95% السياح يمسحون الرمز. نحتفظ بقائمتين ورقيتين احتياطاً." |
| **"Et si internet coupe ?"** | "Menu en cache après premier scan. Ticket thermique sans réseau." | "القائمة محفوظة بعد المسح الأول. الطباعة تعمل بدون إنترنت." |
| **"Je dois réfléchir"** | "Qu'est-ce qui vous ferait avancer ? → identifier le vrai bloqueur" | "ما الذي يساعدك على المضي قدماً؟" |
| **"J'ai déjà un système"** | "Lequel ? On a une API ouverte. On peut s'intégrer." | "أي نظام؟ لدينا API مفتوح. يمكننا الدمج." |

---

## 6. AVANTAGES CONCURRENTIELS vs MARCHÉ MAROCAIN

| Concurrent | Limitation | Avantage DIMA |
|---|---|---|
| Menumate.ma | Menu QR basique, pas d'écosystème | Écosystème complet : génération + lecture + impression + dashboard |
| DigiMenu.ma | SaaS menu uniquement | QR dynamique + hardware intégré + paiement CMI |
| QrCode.ma | Générateur simple, statique | QR dynamique (modifiable après impression) |
| Solutions EU | Prix 3-5× plus élevés | Prix local 50-70% moins cher + support FR/AR sur site |

### Stack technique différenciante
- **Backend** : Django/DRF (Python) — scalable, API-first
- **Frontend** : Vue.js — PWA native, sans téléchargement
- **Hardware** : Terminal Android Zebra/Honeywell + imprimante thermique + douchette
- **Paiement** : CMI intégré (Centre Monétique Interbancaire Maroc)
- **Offline** : Service Worker + cache local — fonctionne en zone faible réseau

---

## 7. PARTENARIATS LOCAUX À ACTIVER

| Partenaire | Intérêt mutuel | Contact type |
|---|---|---|
| **CMI** | Pousse le paiement mobile → DIMA apporte le hardware QR | Responsable développement partenariats |
| **ONMT** | Digitalise l'expérience touristique → DIMA = solution technique | Chef de projet digital |
| **Fournisseurs papier** | Perdent le marché menus papier → proposer une commission | Gérant d'imprimerie locale |
| **Agences événementielles** | Mariages/événements → badges QR + traçabilité | Directeur commercial |

---

## 8. SUIVI POST-DÉMO (J+1 à J+7)

| Jour | Canal | Action |
|---|---|---|
| **J+1** | Email | Fiche offre PDF + contrat 1 page + capture ticket thermique |
| **J+2** | WhatsApp | Vidéo témoignage client 30 sec (partenaire Casablanca) |
| **J+4** | Appel | "Avez-vous des questions ?" — écouter le vrai bloqueur |
| **J+7** | WhatsApp | Dernière relance + rappel offre imprimante + lien Calendly |

### Template WhatsApp J+3 :
```
Salam [Prénom] 👋
Petit rappel offre "Riad Digital" :
✅ Imprimante thermique OFFERTE avant [date]
✅ Installation 48h · Support 7j/7 FR/AR
👉 calendly.com/dimasolutions/installation
Baraka Allah fik 🙏
[Prénom] • Dima Solutions
```

---

## 9. MÉTRIQUES DE SUCCÈS

| KPI | Cible |
|---|---|
| Taux démo → devis | > 70% |
| Taux devis → signature | > 40% |
| Délai closing moyen | < 48h après démo |
| NPS prospect (satisfaction démo) | > 8/10 |
| Leads par semaine (Marrakech) | 3-5 démos/semaine |

---

## 10. LIVRABLES COMMERCIAUX INCLUS

- `DIMA_Flyer_A5_JustForYou.html` — Flyer recto (FR) + verso (AR) imprimable A5
- `DIMA_Pitch_Demo_Interactif_Marrakech.html` — Pitch deck interactif 6 slides + démo chrono
- `DIMA_Demo_Marrakech_Rapport_Complet.md` — Ce rapport (référence terrain)

---

*Document interne — Dima Solutions AI Tech | Version 2.0 — Juin 2026*
*Basé sur : Plan Complet QR Code Dynamique — Groupes A & B*
