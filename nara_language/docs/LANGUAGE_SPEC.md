# 📘 NĀRA Language Specification

---

## 1. Lexical Structure

- Unicode identifiers in Sanskrit (Devanagari) or IAST transliteration
- Comments: `//` for single-line
- Literals: strings in quotes `"..."`, lists in `[item1, item2]`

---

## 2. Grammar (EBNF Style)

```ebnf
program         ::= { agent_decl | task_decl }
agent_decl      ::= "पुरुषः" identifier "अस्ति" "{" trait_block input_decl output_decl "}"
trait_block     ::= "गुणाः" ":" "[" string_list "]"
input_decl      ::= "प्रवेशः" ":" identifier
output_decl     ::= "निर्गमः" ":" identifier
task_decl       ::= "कर्मे" string "यदा:" statement_block
statement_block ::= { conditional | assignment | invocation }
conditional     ::= "यदि" condition ":" statement_block ["अन्यथा:" statement_block]
assignment      ::= identifier "=" expression
invocation      ::= "आह्वानं" identifier "सह" string
```

---

## 3. Core Keywords

| Keyword        | Meaning              |
|----------------|----------------------|
| `पुरुषः`       | Agent declaration    |
| `गुणाः`        | Trait list           |
| `प्रवेशः`      | Input declaration    |
| `निर्गमः`      | Output declaration   |
| `कर्मे`        | Task block           |
| `यदि` / `अन्यथा` | Conditional if/else |
| `प्रत्युपकर्षः`| Feedback loop        |
| `स्मृति`       | Agent memory         |
| `आह्वानं`      | LLM/API invocation   |

---

## 4. Type System

- `string`: `"..."` quoted strings
- `list[string]`: `["a", "b"]`
- `boolean`: implicit from conditional rules
- (future) `pattern`, `intent`, `enum`

---

## 5. Execution Model

- Agents defined by `पुरुषः ... अस्ति`
- Tasks defined with `कर्मे ... यदा:`
- Execution flows via conditionals
- Memory evolves via `स्मृति` and `प्रत्युपकर्षः`

---

## 6. Interpreter Hooks

- Each agent becomes an executable function or coroutine
- Tasks compile into closures with memory context
- Compatible with LLM tools (LangChain, Gemini)

