// NĀRA Interpreter Spec Comments
//
// Grammar Overview (EBNF):
// program         ::= { agent_decl | task_decl }
// agent_decl      ::= "पुरुषः" identifier "अस्ति" "{" trait_block input_decl output_decl "}"
// trait_block     ::= "गुणाः" ":" "[" string_list "]"
// input_decl      ::= "प्रवेशः" ":" identifier
// output_decl     ::= "निर्गमः" ":" identifier
// task_decl       ::= "कर्मे" string "यदा:" statement_block
// statement_block ::= { conditional | assignment | invocation }
// conditional     ::= "यदि" condition ":" block ["अन्यथा:" block]
// assignment      ::= identifier "=" expression
// invocation      ::= "आह्वानं" identifier "सह" string

// Core interpreter logic and AST processing will follow this pattern.
