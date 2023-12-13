import React, { useEffect } from "react";
import {
  MDBContainer,
  MDBRow,
  MDBCol,
  MDBInput,
  MDBBtn,
} from "mdb-react-ui-kit";
import { useState, useRef } from "react";
import { toast } from "react-toastify";
import { useLocation, useNavigate} from "react-router-dom";
import { UserReqType } from "../../types";

export default function EditUser() {
  const [fullName, setFullName] = useState("");
  const [mobNumber, setMobNumber] = useState("");
  const [panNumber, setPanNumber] = useState("");

  const location = useLocation();
  const navigate= useNavigate();

  const updateUser = (e:any) => {
    e.preventDefault();
    let user:UserReqType = {
      // id: location.state.id,
      full_name: fullName,
      mob_number: mobNumber,
      pan_number: panNumber,
    };
    console.log(user);
    toast.success("User Edited Successfully");
    navigate("/allUsers");
  };
  useEffect(() => {
    setFullName(location.state.full_name);
    setMobNumber(location.state.mob_number);
    setPanNumber(location.state.pan_number);
  }, []);

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
                    defaultValue={location.state.full_name}
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
                    defaultValue={location.state.mob_number}
                  />
                  <MDBInput
                    label="PAN Number"
                    // icon="lock"
                    type="text"
                    required
                    onChange={(e) => {
                      setPanNumber(e.target.value);
                    }}
                    defaultValue={location.state.date}
                  />
                </div>
                <div className="text-center mt-3">
                  <MDBBtn
                    color="info"
                    onClick={(e) => {
                      updateUser(e);
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
