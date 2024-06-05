// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/HomePage';
import RestaurantList from './components/Restaurant/RestaurantList';
import RestaurantDetail from './components/Restaurant/RestaurantDetail';
import Login from './pages/Login/login';
import RegisterUser from './pages/Register/registerUser';
import RegisterOwner from './pages/Register/registerOwner';
import OwnerDashboard from './components/OwnerDashboard/OwnerDashboard';
import CreateRestaurant from './components/CreateRestaurant/CreateRestaurant';
import EditRestaurant from './components/EditRestaurant/EditRestaurant';
import ViewRatings from './components/ViewRatings/ViewRatings';
import AddRestaurant from './components/AddRestaurant/AddRestaurant';
import UserReviews from './components/UserReviews/UserReviews'; // Add this line
import { UserProvider } from './components/UserContext/UserContext'; // Add this line

function App() {
  return (
    <UserProvider> {/* Wrap everything in UserProvider */}
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/restaurants" element={<RestaurantList />} />
          <Route path="/restaurant/:id" element={<RestaurantDetail />} />
          <Route path="/register-user" element={<RegisterUser />} />
          <Route path="/register-owner" element={<RegisterOwner />} />
          <Route path="/owner-dashboard" element={<OwnerDashboard />} />
          <Route path="/create-restaurant" element={<CreateRestaurant />} />
          <Route path="/edit-restaurant/:id" element={<EditRestaurant />} />
          <Route path="/view-ratings/:id" element={<ViewRatings />} />
          <Route path="/add-restaurant" element={<AddRestaurant />} />
          <Route path="/my-reviews" element={<UserReviews />} /> {/* Add this line */}
        </Routes>
      </Router>
    </UserProvider>
  );
}

export default App;
