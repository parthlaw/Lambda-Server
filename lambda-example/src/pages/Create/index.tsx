import React from "react";
import {
  MDBContainer,
  MDBRow,
  MDBCol,
  MDBInput,
  MDBBtn,
} from "mdb-react-ui-kit";
import "./Create.css";
import { useState, useRef } from "react";
import { toast } from "react-toastify";
import { useNavigate } from "react-router-dom";
import { UserReqType } from "../../types";

export default function CreateNewUser() {
  const [fullName, setFullName] = useState("");
  const [mobNumber, setMobNumber] = useState("");
  const [panNumber, setPanNumber] = useState("");

  const navigate = useNavigate();

  const createUser = (e:any) => {
    e.preventDefault();
    if (
      fullName === "" ||
      mobNumber === "" ||
      panNumber === ""
    ) {
      alert("Please fill all the fields");
      return;
    }
    let user:UserReqType = {
      full_name: fullName,
      mob_number: mobNumber,
      pan_number: panNumber,
    };
    console.log(user);
    toast.success("User Created Successfully");
    navigate("/allUsers");
  };

  return (
    <div>
      <div className="d-lg-flex justify-content-center align-items-center flex-lg-column w-100 h-100">
        <MDBContainer className="w-75 mh-100 vh-100 h-100">
          <MDBRow>
            <MDBCol>
              <form className="d-flex flex-column justify-content-center align-items-center customHeight">
                <p className="h4 text-center mb-4">Create New User</p>
                <div className="grey-text w-75 d-flex justify-content-evenly align-items-center flex-column h-50">
                  <MDBInput
                    label="Full Name"
                    // icon="user"
                    type="text"
                    // error="wrong"
                    // success="right"
                    required
                    onChange={(e) => {
                      setFullName(e.target.value);
                    }}
                  />
                  <MDBInput
                    label="Mobile Number"
                    // icon="envelope"
                    type="text"
                    // error="wrong"
                    // success="right"
                    required
                    onChange={(e) => {
                      setMobNumber(e.target.value);
                    }}
                  />
                  <MDBInput
                    label="PAN Number"
                    // icon="lock"
                    type="text"
                    required
                    onChange={(e) => {
                      setPanNumber(e.target.value);
                    }}
                  />
                </div>
                <div className="text-center mt-3">
                  <MDBBtn
                    color="info"
                    onClick={(e) => {
                      createUser(e);
                    }}
                  >
                    Save
                  </MDBBtn>
                </div>
              </form>
            </MDBCol>
          </MDBRow>
        </MDBContainer>
      </div>
    </div>
  );
}
