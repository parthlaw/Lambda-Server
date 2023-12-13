import React, { useEffect, useState } from "react";
import Table from "../../Components/Table";
import "./AllUsers.css";
import { useNavigate } from "react-router-dom";
import { UserType } from "../../types";
export default function AllBillPage() {
  const [users,setUsers]=useState<[UserType]>()

  useEffect(() => {
    console.log(users);
  }, [users]);

  const navigation = useNavigate();
  const handleNavigate = () => {
    navigation("/new");
  };

  return (
    <div>
      {users && users.length ? (
        <Table data={users} />
      ) : (
        <div className="d-flex justify-content-center w-100 mt-3">
          No data to display! Create a user first
        </div>
      )}
      <div className="d-flex justify-content-center w-100">
        <button
          className="btn btn-info btnWidth"
          type="button"
          onClick={handleNavigate}
        >
          Create New User
        </button>
      </div>
    </div>
  );
}
