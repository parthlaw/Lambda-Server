import React, { useEffect, useState } from "react";
import {
  MDBBtn,
  MDBTable,
  MDBTableHead,
  MDBTableBody,
} from "mdb-react-ui-kit";
import { useNavigate } from "react-router-dom";
import "./Table.css";
import { UserType } from "../types";
export default function Table({ data }:{data:[UserType]}) {

  const handleDelete = (item:UserType) => {
    console.log(item);
  };

  const navigation = useNavigate();
  const handleEdit = (item:UserType) => {
    console.log(item);
    navigation("/edit", {
      state: {
        id: item.id,
        full_name:item.full_name,
        pan_number:item.pan_number,
        mob_number:item.mob_number
      },
    });
  };

  return (
    <div className="d-flex flex-column align-items-start">
      <MDBTable align="middle">
        <MDBTableHead>
          <tr>
            <th scope="col">Full Name</th>
            <th scope="col">Mobile Number</th>
            <th scope="col">PAN number</th>
          </tr>
        </MDBTableHead>
        <MDBTableBody>
          {data.map((item) => (
            <tr>
              <td>{item.full_name}</td>
              <td>{item.mob_number}</td>
              <td>{item.pan_number}</td>
              <td>
                <MDBBtn
                  color="link"
                  rounded
                  size="sm"
                  onClick={() => handleEdit(item)}
                >
                  Edit
                </MDBBtn>
                <MDBBtn
                  color="link"
                  rounded
                  size="sm"
                  onClick={() => handleDelete(item)}
                >
                  Delete
                </MDBBtn>
              </td>
            </tr>
          ))}
        </MDBTableBody>
      </MDBTable>
    </div>
  );
}
