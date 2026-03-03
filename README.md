# Infinite Socrates

AI-Powered Socratic Learning for STEAM Education

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📚 Project Overview

**Infinite Socrates** is an innovative educational tool that combines the Socratic method with artificial intelligence to help students deepen their understanding of mathematics. The project is part of the **AEIF 2026** initiative, funded by the U.S. Embassy Mexico, and developed by students at Arkansas State University Campus Querétaro (ASUCQ).

The application provides a notepad-style interface where students can write mathematical equations (handwriting recognition) and receive guided, sequential questions that lead them to discover concepts on their own—rather than giving direct answers. A points system tracks progress, and a concept hierarchy (tree) helps the AI adapt questions to the student's level.

This repository contains the full source code, documentation, and development resources for the **Infinite Socrates** platform.

## 👥 Team & Roles

| Name | Role | GitHub |
|------|------|--------|
| Juan Pablo Lago Pizano | Lead Developer (AI integration) | `@juanpablo-lago` |
| Rassim Belazzoug | Backend & Database (Firebase) | `@rassim-belazzoug` |
| Dominick Daly de Loos | Frontend & UI/UX | `@dominick-daly` |
| Dr. Erick Ulin Avila | Faculty Supervisor | `@erickulin` |
| Prof. Sergio Sanchez Padilla | Critical Thinking Advisor | `@sergiosanchez` |
| Dr. Rafael Aguilar Gonzalez | Curriculum & Assessment | `@rafaelaguilar` |

All team members are expected to follow the contribution guidelines below.

## 🛠️ Tech Stack

- **Language**: Python 3.9+
- **Frontend**: Tkinter / PyQt (or web-based with Flask – TBD)
- **Handwriting Recognition**: MyScript / Mathpix API (to be decided)
- **AI Engine**: OpenAI API (GPT-4) for generating Socratic prompts
- **Backend**: Firebase (Firestore for user data, progress, question bank)
- **Dependency Management**: `pip` + `requirements.txt`
- **Version Control**: Git + GitHub (this repository)

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher installed
- Git installed
- A GitHub account (you should already have access to this repo)
- API keys (will be provided separately; never commit them to the repo)

### Initial Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/ASUCQ-Projects/infinite-socrates.git
   cd infinite-socrates

2. Create a virtual environment

bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Install dependencies

bash
pip install -r requirements.txt

4. Set up environment variables

Copy .env.example to .env and fill in your API keys and Firebase configuration.
Never commit .env to the repository.

5. Run the application

bash
python src/main.py

📁 Repository Structure
text
infinite-socrates/
├── .github/                # GitHub templates (issue, PR)
├── docs/                    # Documentation, meeting notes, design docs
├── src/                     # Main source code
│   ├── main.py              # Entry point
│   ├── ui/                  # User interface modules
│   ├── ai/                  # AI prompt generation and handling
│   ├── recognition/         # Handwriting recognition integration
│   ├── database/            # Firebase client and data models
│   ├── models/              # Core classes (User, Session, Question, ConceptTree, ProgressTracker)
│   └── utils/               # Helper functions
├── tests/                   # Unit tests (mirrors src structure)
├── examples/                # Example notebooks/scripts
├── requirements.txt         # Python dependencies
├── .env.example             # Example environment variables
├── .gitignore               # Files/folders to ignore in git
├── LICENSE                  # MIT License
└── README.md                # This file

🔄 Development Workflow
We follow a feature-branch workflow with pull requests and code reviews.

Branching Strategy
main – Production-ready code. Protected; only merged via pull requests after review.

develop – Integration branch for ongoing work. Feature branches are merged here.

feature/<short-description> – Each new feature or task gets its own branch (e.g., feature/handwriting-integration).

bugfix/<short-description> – For bug fixes.

hotfix/<short-description> – For urgent fixes to main.


Step-by-Step Contribution

Pick a task from the GitHub Issues or Project board. Assign it to yourself.

2. Create a new branch from develop:

bash
git checkout develop
git pull origin develop
git checkout -b feature/your-feature-name

3. Write code – follow coding standards (see below). Commit frequently with clear messages.

bash
git add .
git commit -m "Add handwriting recognition module"

4. Push your branch to GitHub:

bash
git push origin feature/your-feature-name

5. Open a Pull Request (PR) against the develop branch.

Fill in the PR template (if any).

Request reviews from at least one other team member.

Link the related issue.

6. Address review comments – make changes, push additional commits.

7. After approval, the PR will be merged by a maintainer.

8. Delete your feature branch (both locally and on GitHub).

Commit Message Guidelines

Use present tense ("Add feature" not "Added feature").

First line: concise summary (max 50 chars).

Optionally, add a more detailed description after a blank line.

Reference issue numbers if applicable: Fixes #12.

Example:

text
Integrate MyScript handwriting API

- Add MyScriptClient class in recognition/myscript.py
- Implement basic handwriting-to-text conversion
- Update main UI to display recognized text
- Add tests for MyScriptClient

Closes #23

✅ Testing & Code Quality
All new features must include unit tests. Place tests in the tests/ directory, mirroring src/.

Run tests locally before pushing:

bash
pytest tests/
We aim for at least 80% code coverage. You can check coverage with:

bash
pytest --cov=src tests/
Code should follow PEP 8 style. Use flake8 or pylint to lint your code.

Write docstrings for all public modules, classes, and functions (Google style recommended).

🧩 Dividing the Work
The project is broken down into several key areas. Use GitHub Issues and the Project board to organize tasks. Here's an initial breakdown:

Core Modules & Responsibilities
Module					Description									Lead
UI (Frontend)				Notepad interface, equation display, question panel, progress bar.		Dominick
Handwriting Recognition			Convert user-drawn equations to machine-readable text/MathML.			Juan Pablo & Dominick)
AI Prompt Engine			Generate Socratic questions based on the equation and student history.		Juan Pablo
Question Bank				Store and retrieve predefined prompts (categorized by topic/difficulty).	Rassim
Concept Tree				Represent math topics hierarchically (prerequisites).				Rassim (with input from faculty)
Progress Tracking			Points system, user profiles, session history (Firebase).			Rassim
Backend Integration			Firebase setup, data models, API endpoints.					Rassim
Testing					Unit tests for each module.							Shared (each writes tests for own code)


Task Breakdown Suggestions
Week 1-2: Setup environment, Firebase project, basic UI skeleton.

Week 3-4: Integrate handwriting API; create simple equation display.

Week 5-6: Build concept tree and question bank; connect to Firebase.

Week 7-8: Develop AI prompt engine (prompt templates, call OpenAI).

Week 9-10: Implement progress tracking and points system.

Week 11-12: Beta testing, bug fixes, polish.


🤝 Cross-Checking & Collaboration
Code Reviews: Every PR must be reviewed by at least one other developer. This ensures quality and knowledge sharing.

Pair Programming: For complex features, consider pairing up.

Weekly Sync: We meet every Monday at 10:00 AM (virtual or in person) to discuss progress, blockers, and next steps.

Documentation: Keep docs/ up to date. If you add a new API endpoint or change a data model, update the relevant documentation.

Testing: Run the full test suite before opening a PR. If you break existing tests, fix them.

🚦 Using GitHub Issues & Projects
All work should be tracked as an Issue. Issues have labels (enhancement, bug, documentation) and are assigned to a team member.

We use a Project board (link) to visualize progress. Columns: To Do, In Progress, Review, Done.

When you start work on an issue, move it to In Progress.

When you open a PR, move the issue to Review (or link the PR).

After merging, the issue should be automatically closed (if you used "Closes #issue" in the PR description) or manually moved to Done.

📦 Building & Deployment
(To be filled once we have a deployment strategy – e.g., packaging as a standalone app, or hosting as a web app.)

📄 License
This project is licensed under the MIT License – see the LICENSE file for details.

🙏 Acknowledgments
U.S. Embassy Mexico for funding through the Alumni Engagement Innovation Fund (AEIF) 2026.

Arkansas State University Campus Querétaro for institutional support.

All faculty and students who contribute to the project.

America250 – celebrating 250 years of American innovation.

Happy coding! If you have questions, reach out on our Slack channel or create a GitHub Issue.

