import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Users from './components/Users';
import Teams from './components/Teams';
import Workouts from './components/Workouts';

const App: React.FC = () => {
    return (
        <div>
            <nav className="navbar navbar-expand navbar-light bg-light">
                <div className="container">
                    <Link className="navbar-brand" to="/">OctoFit</Link>
                    <div className="navbar-nav">
                        <Link className="nav-link" to="/activities">Activities</Link>
                        <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
                        <Link className="nav-link" to="/teams">Teams</Link>
                        <Link className="nav-link" to="/users">Users</Link>
                        <Link className="nav-link" to="/workouts">Workouts</Link>
                    </div>
                </div>
            </nav>
            <div className="container mt-4">
                <Routes>
                    <Route path="/" element={<h2>Welcome to OctoFit Tracker</h2>} />
                    <Route path="/activities" element={<Activities />} />
                    <Route path="/leaderboard" element={<Leaderboard />} />
                    <Route path="/teams" element={<Teams />} />
                    <Route path="/users" element={<Users />} />
                    <Route path="/workouts" element={<Workouts />} />
                </Routes>
            </div>
        </div>
    );
};

export default App;