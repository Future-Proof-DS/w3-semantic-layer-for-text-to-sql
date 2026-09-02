Demo flow
.\scripts\run_chat_schema.ps1 → ask a question in the browser

q01 — "What is total net product revenue for delivered orders?"
q05 — "For delivered orders, what is net product revenue and gross payment value?"
q08 — "What is net product revenue for delivered orders placed in 2018?"

.\scripts\run_eval_schema.ps1 → show baseline score



Open configs/semantic_layer.yaml → explain rules
.\scripts\run_chat_semantic.ps1 → same question, better SQL
.\scripts\run_eval_semantic.ps1 → show improved score



