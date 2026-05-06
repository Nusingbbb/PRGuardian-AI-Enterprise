
import React, {useEffect, useState} from "react";

export default function Dashboard(){
 const [reviews,setReviews]=useState([]);
 useEffect(()=>{
   fetch("http://localhost:8000/reviews").then(r=>r.json()).then(setReviews);
 },[]);
 return (
  <div style={{padding:30,fontFamily:"Arial"}}>
   <h1>PRGuardian AI Pro Control Center</h1>
   <h3>Total Reviews: {reviews.length}</h3>
   {reviews.map((r,i)=>(
    <div key={i} style={{border:"1px solid #ccc",marginBottom:20,padding:20}}>
      <h2>{r.message}</h2>
      <p>Risk: {r.risk_level}</p>
      <p>Issues: {r.issues_found}</p>
      <p>Patches: {r.patches_generated}</p>
      <pre>{JSON.stringify(r,null,2)}</pre>
    </div>
   ))}
  </div>);
}
