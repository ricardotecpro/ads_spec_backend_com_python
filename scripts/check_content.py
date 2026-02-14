import glob
import re
import os

def check_lesson(lesson_num):
    lesson_str = f"{lesson_num:02d}"
    
    # Paths
    content_path = f"docs/{lesson_str}.md"
    slide_path = f"docs/slides/{lesson_str}-slides.md"
    quiz_path = f"docs/quizzes/quiz-{lesson_str}.md"
    exercise_path = f"docs/exercicios/exercicios-{lesson_str}.md"
    project_path = f"docs/projetos/projeto-{lesson_str}.md"
    
    report = {
        "lesson": lesson_str,
        "content_exists": os.path.exists(content_path),
        "mermaid_count": 0,
        "slides_exists": os.path.exists(slide_path),
        "slides_revealjs": False,
        "quiz_exists": os.path.exists(quiz_path),
        "quiz_questions": 0,
        "exercises_exists": os.path.exists(exercise_path),
        "project_exists": os.path.exists(project_path),
        "project_has_tests": False,
        "project_has_pytest": False
    }

    # Check Content & Mermaid
    if report["content_exists"]:
        with open(content_path, 'r', encoding='utf-8') as f:
            content = f.read()
            report["mermaid_count"] = content.count('```mermaid')

    # Check Slides
    if report["slides_exists"]:
        with open(slide_path, 'r', encoding='utf-8') as f:
            slides = f.read()
            if 'layout: revealjs' in slides:
                report["slides_revealjs"] = True

    # Check Quiz
    if report["quiz_exists"]:
        with open(quiz_path, 'r', encoding='utf-8') as f:
            quiz = f.read()
            # Count questions (lines starting with number followed by dot)
            questions = re.findall(r'^\d+\.', quiz, re.MULTILINE)
            report["quiz_questions"] = len(questions)

    # Check Project
    if report["project_exists"]:
        with open(project_path, 'r', encoding='utf-8') as f:
            project = f.read()
            if "test" in project.lower() or "teste" in project.lower():
                report["project_has_tests"] = True
            if "pytest" in project.lower():
                report["project_has_pytest"] = True

    return report

print(f"{'Aula':<5} | {'Mermaid':<8} | {'Slides (Rev)':<12} | {'Quiz (Qtd)':<10} | {'Proj Tests':<10} | {'Pytest':<6}")
print("-" * 70)

issues = []

for i in range(1, 17):
    r = check_lesson(i)
    
    mermaid_status = "✅" if r["mermaid_count"] > 0 else "❌"
    slide_status = "✅" if r["slides_revealjs"] else "❌"
    quiz_val = r["quiz_questions"]
    quiz_status = f"✅ ({quiz_val})" if quiz_val >= 5 else f"❌ ({quiz_val})"
    
    proj_test_status = "-"
    if i >= 9:
        proj_test_status = "✅" if r["project_has_tests"] else "❌"
    
    pytest_status = "-"
    if i == 16:
        pytest_status = "✅" if r["project_has_pytest"] else "❌"

    print(f"{r['lesson']:<5} | {mermaid_status} {r['mermaid_count']:<4} | {slide_status:<12} | {quiz_status:<10} | {proj_test_status:<10} | {pytest_status:<6}")

    if r["mermaid_count"] == 0:
        issues.append(f"Aula {r['lesson']}: Missing Mermaid diagram")
    if not r["slides_revealjs"]:
        issues.append(f"Aula {r['lesson']}: Slides not RevealJS configured")
    if r["quiz_questions"] < 5:
        issues.append(f"Aula {r['lesson']}: Quiz has less than 5 questions")
    if i >= 9 and not r["project_has_tests"]:
        issues.append(f"Aula {r['lesson']}: Project missing basic tests content")
    if i == 16 and not r["project_has_pytest"]:
        issues.append(f"Aula {r['lesson']}: Lesson 16 Project missing pytest")

if issues:
    print("\nISSUES FOUND:")
    for issue in issues:
        print(f"- {issue}")
else:
    print("\nALL CHECKS PASSED!")
