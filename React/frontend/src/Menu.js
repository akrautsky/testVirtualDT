import React, { useContext, useEffect, useState } from 'react';
import axios from 'axios';
import './Menu.css';
import microphoneGif from './microphone.gif'; // Make sure to place the microphone.gif file in the src folder
import { MyOrderContext } from './myOrderContext';
import io from 'socket.io-client';

function Menu() {
  const { myOrder, setMyOrder } = useContext(MyOrderContext);
  

  useEffect(() => {
    console.log('myOrder in Menu updated:', myOrder);
  }, [myOrder]);


  useEffect(() => {
    const newSocket = io('http://localhost:5001', {
      transports: ['websocket'],  // Specify WebSocket as the transport
    });

    // Check if the connection is successful
    newSocket.on('connect', () => {
      console.log('WebSocket connected');
    });

    // Listen for messages from the server
    newSocket.on('current_order', (data) => {
      console.log('Received message from server:', data.items);
      // setMyOrder(data.myOrder);
      // setting the current order to the context
      if(data.items.length > 0){
        setMyOrder(data.items);
      }
      
    });

    return () => {
      if (newSocket) {
        newSocket.close();
      }
    };
  } );
  
  

  const dummyMenu = [
    { section: 'Appetizers', items: [
      { name: 'Spring Rolls', price: '$5.00' },
      { name: 'Garlic Bread', price: '$4.00' },
      { name: 'Bruschetta', price: '$6.00' },
      { name: 'Stuffed Mushrooms', price: '$7.00' }
    ]},
    { section: 'Smoothies', items: [
      { name: 'Mango Smoothie', price: '$6.00' },
      { name: 'Berry Blast', price: '$6.50' },
      { name: 'Green Detox', price: '$7.00' },
      { name: 'Banana Honey', price: '$6.00' }
    ]},
    { section: 'Pizzas', items: [
      { name: 'Margherita', price: '$12.00' },
      { name: 'Pepperoni', price: '$14.00' },
      { name: 'BBQ Chicken', price: '$15.00' },
      { name: 'Veggie Delight', price: '$13.00' }
    ]}
  ];

  const getMyOrder = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:5000/api/myOrder/getMyOrder");
      console.log('Response data:', response.data);
      setMyOrder(response.data.myOrder); // Update the context state
    } catch (error) {
      console.log(error);
    }
  }

  // adding the event listener to get data from the server


  return (
    <div className="menu-section">
      <h2 className="menu-header">Menu</h2>
      <div className="menu-items-container">
        {dummyMenu.map((category, index) => (
          <div key={index} className="menu-category">
            <h3>{category.section}</h3>
            <ul className="menu-items">
              {category.items.map((item, idx) => (
                <li key={idx} className="menu-item">
                  <span>{item.name}</span>
                  <span>{item.price}</span>
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
      <div className="menu-footer">
        <img src={microphoneGif} alt="Microphone" className="microphone-gif" onClick={getMyOrder}/>
      </div>
    </div>
  );
}

export default Menu;
