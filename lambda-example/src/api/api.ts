import axios from "axios"
import { UserType } from "../types"

const BASE_URL="https://aa4jkqbo36.execute-api.eu-north-1.amazonaws.com"

export const create_user=async(user:UserType)=>{
  try{
    const resp = await axios.post(`${BASE_URL}/create_user`,user)
    return resp.data
  }catch(err){
    console.log(err)
    throw err
  }
}
export const get_users=async()=>{
  try{
    const resp = await axios.get(`${BASE_URL}/get_users`)
    return resp.data
  }catch(err){
    console.log(err)
    throw err
  }
}
export const update_user=async(user_id:string,update_data:UserType)=>{
  try{
    const resp = await axios.patch(`${BASE_URL}/update_user/${user_id}`,update_data)
    return resp.data
  }catch(err){
    console.log(err)
    throw err
  }
}
export const delete_user=async(user_id:string)=>{
  try{
    const resp = await axios.delete(`${BASE_URL}/delete_user/${user_id}`)
    return resp.data
  }catch(err){
    console.log(err)
    throw(err)
  }
}
