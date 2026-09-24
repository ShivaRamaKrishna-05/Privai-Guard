const API = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000/api/v1";
export async function api(path,options={}){
 const token=localStorage.getItem("token");
 const headers={"Content-Type":"application/json",...(options.headers||{})};
 if(token) headers.Authorization=`Bearer ${token}`;
 const res=await fetch(`${API}${path}`,{...options,headers});
 const data=await res.json().catch(()=>({}));
 if(!res.ok) throw new Error(data.detail||data.error||"Request failed");
 return data;
}
