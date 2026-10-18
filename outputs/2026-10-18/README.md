Full-resolution files: https://github.com/cherryland32/dlblp-creatives/tree/main/outputs/2026-10-18

# Weekly ad batch - 2026-10-18

10 Meta creatives for "De la Bobiță la Pepene" - Setul 2 în 1, **419 lei** (redus de la **548 lei**),
**Economisești 129 lei**, **Livrare gratuită**. 9 remixes of the proven recipe pool + 1 new concept.
Statics are 1080x1350 JPEG q94. Produced with pure PIL from repo assets - Higgsfield was available
(1861.8 credits on the account at time of production) but not called this week: the repo's pre-approved
real product photos and generated scenes already satisfy the "real covers, no AI redesign" rule, so no
new generation was needed.

Per the PERFORMANCE SIGNALS note in the playbook (the WhatsApp chat static drove the account's first
tracked sale), this batch again weights toward chat/screen-UI formats: 4 of the 10 creatives are
fake-UI/screen-life (2 of them chat apps never used before in this account - Telegram and Viber).

| # | File | Recipe / angle | Notes |
|---|------|-----------------|-------|
| 01 | `01_telegram_bunici.jpg` | Fake-UI chat | Telegram group chat **"Bunicii"** - grandparents (bunica Rodica, tata mare) planning the gift together. New app, new participant angle (grandparents as chatters, not used before). |
| 02 | `02_screen_time.jpg` | Fake-UI | **NEW CONCEPT**: iOS Screen Time weekly-report screen (bar chart of hours per day + per-app breakdown) contrasted with "15 minute pe săptămână ca să nu uiți nimic." Not used in any prior batch. |
| 03 | `03_viber_chat.mp4` | Screen-life VIDEO (chat) | 1080x1920, 30fps, 13.67s, libx264 crf18 +faststart, `music.mp3` bed with 0.5s fade-in / 0.6s fade-out. Animated **Viber**-style chat (new app chrome, new friend "Bianca") - reuses the proven gift-chat structure (price reveal, photo bubble, end card) on a platform never used before in this account. |
| 04 | `04_cover_split.jpg` | Generated base + typographic overlay | `product_cover.jpg` used as a hero for the first time, in a new half-split layout (photo left / copy block right) - distinct from the full-bleed-with-gradient treatments used in prior weeks. |
| 05 | `05_torn_paper_poster.jpg` | Typographic poster | New visual treatment: a torn-paper / deckle-edge card on solid sage, new headline "Hârtia nu se actualizează. Ea rămâne." |
| 06 | `06_folk_ribbon.jpg` | Folk/Romanian aesthetic | New mechanic: horizontal embroidered-ribbon bands (top + bottom) framing `album_ref.jpg`, distinct from the corner-motif frame, diamond-border invitation and flat cross-stitch poster used in prior batches. New headline "De la bunica la mama, de la mama la tine." |
| 07 | `07_claim_card_photo.jpg` | Emotional claim card | New composition: full-bleed `bump.png` photo (not a flat-color card) with a single bold-word headline ("Uită.") + the approved Ebbinghaus line. |
| 08 | `08_parcel_tracking.jpg` | Fake-UI / free-shipping angle | New mechanic: a parcel-tracking app screen using `base_delivery.png` (unused in the last two batches), with a delivery-status timeline ending in "Livrat - 1-2 zile lucrătoare" and "Livrare gratuită" badge. |
| 09 | `09_album_pages.jpg` | Generated base + overlay (legacy angle) | Fanned/layered page spreads (`page_05_week8.jpg` + `album_spread_a9370.jpg`) under the headline "Nouă luni într-o carte. Și încă 21 de luni după." - new composition vs. the single full-bleed hero treatments used before. |
| 10 | `10_before_after.jpg` | Typographic poster | New split-screen mechanic: "ACUM" (phone photo grid, 3.000 de poze netipărite) vs. "PESTE 20 DE ANI" (`kf_s7_both_books.png`), closing on "Alege ce rămâne." |

`contact_sheet.jpg` - all 10 creatives (video represented by a frame grabbed at 6.5s) for review.

## Self-review checklist
- Legibility at thumbnail size: checked via contact sheet, all headlines/prices readable.
- Margins: no text clipped against frame edges. Self-review caught and fixed three real bugs before
  finalizing: (1) `01_telegram_bunici` - the chat thread overflowed into the footer price panel, fixed by
  trimming the conversation and shrinking the photo-bubble size; (2) `06_folk_ribbon` - the headline, price
  block and bottom embroidery band all overlapped due to a layout computed from both top and bottom
  simultaneously, rewritten as a single top-to-bottom sequential layout; (3) the Viber video script
  (`build_video.py`) had several lines of dialogue typed without diacritics ("ca"/"sa"/"si"/"ii"/"il"
  instead of "că"/"să"/"și"/"îi"/"îl" etc.) - caught on frame inspection and corrected, then frames and
  the final .mp4 were regenerated.
- Prices: 419 lei / 548 lei crossed / Economisești 129 lei present on all 10 creatives.
- Livrare gratuită: present on all 10 creatives.
- Diacritics: verified ăâîșț render correctly with EBGaramond-Bold/Italic and Inter-Regular (no Cormorant
  used); scanned all source copy for stray non-ASCII and for words missing diacritics (see bug #3 above).
- No tofu: no emoji glyphs used anywhere (grep-verified); hearts/icons are hand-drawn vector shapes.
- No em dash: grep-verified across all ad-copy source, only "-" used.
- Covers accurate: only repo photos/pre-approved generated assets used (`product_cover.jpg`, `album_ref.jpg`,
  `prod_9151.jpg`, `base_delivery.png`, `bump.png`, `cutout_giftbox.png`, `page_05_week8.jpg`,
  `album_spread_a9370.jpg`, `kf_s7_both_books.png`), no AI redesign of covers.
- Claims: only the verified claims list + the approved Ebbinghaus line; no invented statistics or
  testimonials about the brand. Fake-UI chrome numbers (screen-time hours, delivery timeline, follower-style
  counts) are scenario flavor for the mockups, not brand claims, consistent with prior batches.

## Flags
- Higgsfield balance checked (1861.8 credits available) but not called this week - not needed, see note
  above; no credits were consumed.
- Video audio: `assets/music.mp3` trimmed to 13.67s with 0.5s fade-in / 0.6s fade-out.
