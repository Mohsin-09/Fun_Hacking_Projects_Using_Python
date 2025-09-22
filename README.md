# Hacking Learning Pack (Ethical & Defensive)

**Important:** This pack is for ethical learning and defensive purposes only.  
Do **NOT** use any content here to attack, scan, or access systems you do not own or have explicit permission to test.  
Run everything locally in an isolated environment (VM, sandbox, or container).

## Overview
This repository contains **50 benign, educational** files (Python scripts, static HTML examples, and markdown guides) that illustrate common security concepts and how to defend against them.  
Each item is intentionally safe, contains explanatory comments, and highlights insecure patterns alongside their secure fixes.

## Requirements
- Python 3.8+ for Python examples.
- A modern browser for HTML files.
- Recommended: run in a VM, container, or otherwise isolated environment.

## Quick Start
1. Read this README and the comments at the top of each file.
2. Unzip the archive and `cd` into the folder.
3. Run Python examples locally, e.g.:
   ```bash
   python3 01_hashing.py
   ```
4. Inspect outputs and read the markdown notes before running scripts that intentionally demonstrate insecure patterns.
5. Never run network scans or exploit code against systems you don't own or have permission to test.

## Files Included
01. 01_hashing.py — Shows salted PBKDF2 hashing using hashlib + secrets.  
02. 02_password_strength.py — Basic password strength estimator and recommendations.  
03. 03_hmac_example.py — HMAC demonstration and safe verification using compare_digest.  
04. 04_xor_demo.py — Toy XOR cipher showing why standard crypto libraries are needed.  
05. 05_file_handling.py — Atomic write pattern using temporary files and replace.  
06. 06_sql_demo.py — Local SQLite demo showing SQL injection vulnerability and parameterized query fix.  
07. 07_input_validation.py — Whitelist-based username validation example.  
08. 08_xss_vulnerable.html / 08_xss_sanitized.html — Static HTML examples for XSS teaching.  
09. 09_csrf_token.py — Illustrative CSRF token generator and notes about secure usage.  
10. 10_rate_limit.py — Demo of rate limiting logic to mitigate brute-force attempts.  
11. 11_bruteforce_sim.py — Simulated brute-force defense with temporary account lockout.  
12. 12_secure_cookies.md — Explains Secure/HttpOnly/SameSite cookie flags.  
13. 13_subprocess_safe.py — Shows why to avoid shell=True and pass argument lists.  
14. 14_path_traversal.py — Path traversal detection using resolved paths and whitelist approach.  
15. 15_logging.py — Logging example and warning to avoid logging sensitive data.  
16. 16_config_env.py — Use environment variables for secrets.  
17. 17_tls_note.md — Explanation of TLS importance and best practices.  
18. 18_safe_serialization.py — Demonstrates risks of pickle and suggests safer alternatives.  
19. 19_secure_random.py — Use secrets for cryptographic randomness.  
20. 20_csp.md — CSP header examples and notes.  
21. 21_password_reset.md — Secure design checklist for password reset flows.  
22. 22_oauth.md — Practical OAuth security pointers.  
23. 23_headers.md — Lists important HTTP headers for security hardening.  
24. 24_insecure_deser.md — Explanation and defenses for insecure deserialization.  
25. 25_least_privilege.md — Principle of least privilege explanation.  
26. 26_prepared_sql.py — Another example showing parameterized queries.  
27. 27_code_audit.md — Security-focused code review checklist.  
28. 28_deps.md — Dependency hygiene and vulnerability scanning advice.  
29. 29_file_upload.md — Secure file upload practices.  
30. 30_token_revocation.py — Example token revocation pattern.  
31. 31_cors.md — CORS misconfiguration explanation and safe setup tips.  
32. 32_defense_in_depth.md — Overview of defense-in-depth strategy.  
33. 33_2fa.md — 2FA/TOTP implementation notes and best practices.  
34. 34_error_handling.py — Demonstrates safe error handling patterns.  
35. 35_db_privilege.md — Database least-privilege guidance.  
36. 36_backups.md — Backup security checklist.  
37. 37_safe_defaults.md — Secure default configuration recommendations.  
38. 38_session_mgmt.md — Session management best practices.  
39. 39_monitoring.md — Monitoring and alerting overview.  
40. 40_tmp_files.md — Secure temporary file handling guidance.  
41. 41_os_command.py — Shows safe subprocess usage vs unsafe shell concatenation.  
42. 42_rate_limit_file.py — Very basic file-backed rate limit counter.  
43. 43_requests_tls.md — Reminder to verify TLS certificates with HTTP clients.  
44. 44_use_bcrypt.md — Recommends modern password hashing libraries like bcrypt/argon2.  
45. 45_threat_model.md — Basic threat modeling checklist.  
46. 46_dep_scan.py — Suggests tools for scanning Python dependencies for known vulnerabilities.  
47. 47_rce.md — Warning about remote code execution and safe sandboxing recommendations.  
48. 48_file_perms.md — File permission hygiene and automation tips.  
49. 49_backup_encrypt.md — Example backup encryption command and key management notes.  
50. 50_final_checklist.md — Final deployment security checklist.  
