import { useEffect, useState } from "react";

 function WebSocketPage() {
  const [message, setMessage] = useState("");
  const [input, setInput] = useState("");

  // Create WebSocket connection to FastAPI
  const socket = new WebSocket("ws://127.0.0.1:8000/ws");
  useEffect(() => {

    socket.onopen = () => {
      console.log("Connected to WebSocket server");
    };

    socket.onmessage = (event) => {
      setMessage(event.data); // Display the server response
    };

    socket.onerror = (error) => {
      console.error("WebSocket error:", error);
    };

    // Clean up the connection when the component is unmounted
    return () => {
      socket.close();
    };
  }, []);

  const sendData = () => {
    const packetData = input; // Example: 'tcp,80,80,10' (replace with actual packet data)
    socket.send(packetData);
  };

  return (
    <div>
      <h1>WebSocket Connection</h1>
      <div>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Enter packet data"
        />
        <button onClick={sendData}>Send Data</button>
      </div>
      <p>Response from backend: {message}</p>
    </div>
  );
}

export default WebSocketPage