# 📘 Learn NĀRA: A Language for AI Intention

Welcome to **NĀRA**, a Sanskrit-first language for programming conscious agents.

---

## 🧠 Core Syntax

| Sanskrit     | Meaning        |
|--------------|----------------|
| `पुरुषः`     | agent          |
| `गुणाः`      | traits         |
| `प्रवेशः`     | input          |
| `निर्गमः`     | output         |
| `कर्मे`      | task           |
| `यदि`        | if             |
| `अन्यथा`     | else           |
| `प्रत्युपकर्षः`| feedback loop  |
| `स्मृति`     | memory         |

---

## 🔁 Example: Recursion

```nara
यदि फलम् != "सन्तुलितम्" तर्हि प्रत्युपकर्षं कृत्वा शिक्षां कुरु
```

---

## 🧪 Practice Agent 1: Teacher

```nara
पुरुषः शिक्षकः अस्ति {
    गुणाः: ["धैर्य", "ज्ञान", "पुनरावृत्ति"]
    प्रवेशः: छात्र_प्रश्नः
    निर्गमः: उत्तरम्
}

कर्मे "ज्ञानप्रश्नं उत्तर" यदा:
    यदि छात्र_प्रश्नः.contains("सूत्रम्"):
        उत्तरम् = "विद्या ददाति विनयं"
    अन्यथा:
        उत्तरम् = "प्रश्नं पुनः विश्लेष्यताम्"
```

---

## 🌌 Next

- Try building your own `राजदूतः`, `वैद्यः`, or `योगाचार्यः`
- Add `स्मृति` tracking to create learning agents
- Use the in-browser tutorial for guided missions

🙏 Join the movement: https://discord.gg/TvdkgtZT
