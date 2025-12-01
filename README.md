# Dokumentasi Odoo 17 — Server Framework 101

## Chapter 1: Architecture Overview
- Odoo terdiri dari 3 layer: UI, Business Logic (Python/ORM), Database (PostgreSQL).
- Semua fitur dibungkus sebagai modul.
- Komponen modul: models, views, data, security, controllers, static.
- ORM mengelola tabel & CRUD otomatis.
- Struktur modul:


module
├── models
│   ├── *.py
│   └── __init__.py
├── data
│   └── *.xml
├── __init__.py
└── __manifest__.py
- Modul saling extensible & modular.

---

## Chapter 2: A New Application
- Membuat modul baru dari template kosong.
- Isi minimal:
- `__manifest__.py` → metadata & daftar dependensi.
- `__init__.py` → load folder models.
- folder `models/` berisi file Python model awal.
- Install modul via Apps setelah struktur dasar lengkap.

---

## Chapter 3: Models and Basic Fields
- Model = class Python yang extend `models.Model`.
- Field dasar: `Char`, `Text`, `Boolean`, `Integer`, `Float`, `Date`, `Datetime`.
- `_name` menentukan nama model → jadi nama tabel database.
- Record dibuat otomatis lewat ORM.
- Field memiliki atribut: `required`, `default`, `help`, `readonly`.

---

## Chapter 4: Security — A Brief Introduction
- Security file:
- `ir.model.access.csv` → hak akses CRUD per model.
- Record rules → membatasi record per user.
- Minimal: setiap model harus punya access rule agar tidak error.
- Level access: read, write, create, unlink.

---

## Chapter 5: Finally, Some UI to Play With
- Membuat menu & action agar model bisa muncul di UI.
- Gunakan file XML:
- `ir.ui.menu` untuk menu/submenu.
- `ir.actions.act_window` untuk membuka model.
- Struktur dasar file:
- menu utama → submenu → action → view.

---

## Chapter 6: Basic Views
- Jenis view utama:
- **Tree** (list)
- **Form**
- **Search**
- **Kanban**
- View ditulis dalam XML dan ditautkan via action.
- Field ditampilkan menggunakan tag `<field name="..."/>`.
- Gunakan `arch` di dalam `<record model="ir.ui.view">`.

---

## Chapter 7: Relations Between Models
- Relational fields:
- `Many2one` → foreign key.
- `One2many` → list relasi terbalik.
- `Many2many` → tabel relasi tambahan.
- Domain dapat digunakan untuk filtering record.
- Relasi antar model membantu membangun struktur data lengkap.

---



## Chapter 8: Computed Fields And Onchanges

## Chapter 9: Ready For Some Action?

## Chapter 10: Constraints

## Chapter 11: Add The Sprinkles

## Chapter 12: Inheritance

## Chapter 13: Interact With Other Modules

## Chapter 14: A Brief History Of QWeb

## Chapter 15: The final word