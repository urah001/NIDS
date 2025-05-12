import Link from "next/link";
import React from "react";

export default function Page(){
  return (
    <div>
      <h1>started a new nids</h1>
      view WebSocket :
      <Link href={"/websocket"}> click me to see them </Link>
    </div>
  );
};
