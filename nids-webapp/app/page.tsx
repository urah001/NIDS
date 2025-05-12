import Link from "next/link";
import React from "react";

export const page = () => {
  return (
    <div>
      <h1>started a new nids</h1>
      view WebSocket
      <Link href={"/WebSocket"}></Link>
    </div>
  );
};
