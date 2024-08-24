import React, { useState } from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import orderGif from './order.gif'; // Make sure to place the GIF file in the src folder
import Modal from './Modal';

function App() {
  const [showModal, setShowModal] = useState(false);

  const startOnlineOrder = () => {
    setShowModal(true);
  };

  const handleCloseModal = () => {
    setShowModal(false);
  };

  return (
    <div className="App">
      {!showModal && (
        <img
          src={orderGif}
          className="order-gif"
          alt="Order Online"
          onClick={startOnlineOrder}
        />
      )}
      {showModal && <Modal onClose={handleCloseModal} />}
    </div>
  );
}

export default App; 


// import React, { useEffect, useState } from 'react';
// import io from 'socket.io-client';

// const App = () => {
//   const [message, setMessage] = useState('');
//   const [response, setResponse] = useState('');

//   useEffect(() => {
//     // Connect to the WebSocket server
//     const socket = io('http://localhost:5008'); // Make sure the port matches your Flask app

//     // Listen for connection
//     socket.on('connect', () => {
//       console.log('Connected to WebSocket server');
//     });

//     // Listen for messages from the server
//     socket.on('message', (data) => {
//       console.log('Received message from server:', data);
//       setResponse(data.data);
//     });

//     // Listen for server response to client messages
//     socket.on('server_message', (data) => {
//       console.log('Received server message:', data);
//       setResponse(data.data);
//     });

//     // Clean up the connection when the component unmounts
//     return () => {
//       socket.disconnect();
//     };
//   }, []);

//   const sendMessage = () => {
//     const socket = io('http://localhost:5008');
//     socket.emit('client_message', { data: message });
//   };

//   return (
//     <div>
//       <h1>WebSocket Client</h1>
//       <input 
//         type="text" 
//         value={message}
//         onChange={(e) => setMessage(e.target.value)}
//         placeholder="Type a message..."
//       />
//       <button onClick={sendMessage}>Send Message</button>
//       <p>Response from server: {response}</p>
//     </div>
//   );
// };

// export default App;
