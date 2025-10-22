# OctoFit Tracker

## Overview

The OctoFit Tracker is a fitness application designed to help users track their activities, manage teams, and compete on leaderboards. The app provides personalized workout suggestions and allows for user authentication and profile management.

## Project Structure

The project is organized into two main directories: `backend` and `frontend`.

### Backend

The backend is built using Django and includes the following components:

- **manage.py**: Command-line utility for interacting with the Django project.
- **requirements.txt**: Lists the required Python packages for the project.
- **octofit_tracker/**: Contains the main Django application files, including settings, URLs, and WSGI/ASGI configurations.
- **apps/**: Contains various Django apps for users, activities, teams, and leaderboard functionalities.

### Frontend

The frontend is built using React and includes:

- **package.json**: Configuration file for npm, listing dependencies and scripts.
- **tsconfig.json**: TypeScript configuration file.
- **public/**: Contains the main HTML file for the application.
- **src/**: Contains the main application code, including components and entry point.

## Setup Instructions

### Backend Setup

1. **Create a Python Virtual Environment**:
   ```bash
   python3 -m venv backend/venv
   ```

2. **Activate the Virtual Environment**:
   ```bash
   source backend/venv/bin/activate
   ```

3. **Install Required Packages**:
   ```bash
   pip install -r backend/requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python backend/manage.py migrate
   ```

5. **Start the Development Server**:
   ```bash
   python backend/manage.py runserver
   ```

### Frontend Setup

1. **Install Frontend Dependencies**:
   ```bash
   cd frontend
   npm install
   ```

2. **Start the Frontend Development Server**:
   ```bash
   npm start
   ```

## Features

- User authentication and profiles
- Activity logging and tracking
- Team creation and management
- Competitive leaderboard
- Personalized workout suggestions

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.