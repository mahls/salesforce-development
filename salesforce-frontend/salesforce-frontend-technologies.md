# 🌐 Salesforce Front-End Development Overview

This document outlines the primary front-end technologies used in Salesforce development, including modern and legacy frameworks.

---

## ⚡ What Is the Front-End in Salesforce?

The front-end of Salesforce development is called **Lightning**, which consists of a modern UI framework and tools for building user interfaces within Salesforce.

---

## 🧩 Core Front-End Technologies

### 1. 🔧 Lightning Web Components (LWC)

- **What it is:** A modern front-end framework built on web standards (HTML, CSS, JavaScript).
- **Use Case:** Building custom components for high-performance, scalable Salesforce UIs.
- **Why use it:** Faster, more efficient, and aligned with web industry standards.
- **Status:** ✅ *Recommended standard*

---

### 2. 🌀 Aura Components

- **What it is:** The predecessor to LWC, built specifically for Salesforce.
- **Use Case:** Still used in some orgs and for compatibility reasons.
- **Why use it:** Needed for some legacy functionality or when working in older orgs.
- **Status:** ⚠️ *Legacy but supported*

---

### 3. 🎨 Lightning App Builder

- **What it is:** A drag-and-drop UI tool in Salesforce for building pages using components.
- **Use Case:** Used by both developers and admins to lay out pages.
- **Why use it:** Speeds up UI assembly without coding.
- **Status:** ✅ *Active and widely used*

---

### 4. 🌐 Visualforce

- **What it is:** A tag-based markup language (like HTML) for creating custom pages.
- **Use Case:** Building custom UIs before Lightning was introduced.
- **Why use it:** Still useful for some admin interfaces or legacy pages.
- **Status:** 🛑 *Legacy*

---

## ✅ Summary Table

| Technology               | Type                 | Status              |
|--------------------------|----------------------|---------------------|
| Lightning Web Components | Component Framework  | ✅ Modern standard  |
| Aura Components          | Component Framework  | ⚠️ Legacy           |
| Lightning App Builder    | UI Configuration Tool| ✅ Active            |
| Visualforce              | Page Markup Language | 🛑 Legacy            |

---

## 🧠 Recommendation

If you're beginning front-end development in Salesforce today, focus on learning:

- **Lightning Web Components (LWC)**
- **Using Lightning App Builder to compose UIs**

Legacy tools like Aura and Visualforce are still supported but are generally being phased out in favor of more modern approaches.

---

*Last updated: 2025-05-24*
