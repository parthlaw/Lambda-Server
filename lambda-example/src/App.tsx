import React from "react";
import "./App.css";
import { Route, BrowserRouter, Routes } from "react-router-dom";
import CreateNewBill from "./pages/Create";
import AllBillPage from "./pages/AllUsers";
import { ToastContainer } from "react-toastify";
import EditBill from "./pages/Edit";
import "react-toastify/dist/ReactToastify.css";
function App() {
  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<AllBillPage />} />
          <Route path="/new" element={<CreateNewBill />} />
          <Route path="/allUsers" element={<AllBillPage />} />
          <Route path="/edit" element={<EditBill />} />
        </Routes>
      </BrowserRouter>
      <ToastContainer
        position="top-center"
        autoClose={3000}
        hideProgressBar={false}
        theme="dark"
      />
    </div>
  );
}

export default App;
