import React, { useContext, useState, useEffect } from 'react';
import './CurrentOrder.css';
import orderGif from './yourOrder.gif'; // Make sure to place the yourOrder.gif file in the src folder
import speakerGif from './speaker.gif'; // Make sure to place the speaker.gif file in the src folder
import { MyOrderContext } from './myOrderContext';
//import axios from 'axios';
import io from 'socket.io-client';

function CurrentOrder() {
  const { myOrder } = useContext(MyOrderContext);

  const [total, setTotal] = useState(0);
  const [tip, setTip] = useState(0);
  const [rounded$, setRounded] = useState(0);

  console.log('myOrder from current order', myOrder);


  

  useEffect(() =>{

    const socketIo = io('http://localhost:5001', 
      {
        transports: ['websocket'],  // Specify WebSocket as the transport
      }
    )

    socketIo.on('connect', () => { console.log('WebSocket connected'); });
    socketIo.on('order_summary', (data) => {
      console.log('Received message from tip server:', data.items);
      const orderSummaryData = data.items;
      if( orderSummaryData){
        setTotal(orderSummaryData.total);
        setTip(orderSummaryData.tip_amount);
        setRounded(orderSummaryData.roundedDollar)
        
      }
      
    });


    return () => {
      if (socketIo) {
        socketIo.close();
    };
  };
  }
)


  





  const dummyOrderItems = Array.from({ length: 15 }, (_, i) => ({ item: `Item ${i + 1}` }));

  return (
    <div className="order-section">
      <h2 className="order-header">
        <img src={orderGif} alt="Your Order" className="my-order-gif" />
        Your Order
      </h2>
      <div className="order-items-container">
        <ul className="order-items">
        {myOrder && myOrder.length > 0 ? (
            myOrder.map((order, index) => (
              <li key={index} className="order-item">
                {order.item}: {order.quantity}
              </li>
            ))
          )  : (
            dummyOrderItems.map((item, index) => (
              <li key={index} className="order-item">
                {item.item}
              </li>
            ))
          )}
        </ul>
      </div>
      <div className="order-summary">
        <h5><strong>Order Summary</strong></h5>
        <table className="summary-table">
          <tbody>
            <tr>
              <td>Total: ${total}</td>
              <td>Tip: ${tip}</td>
            </tr>
            <tr>
              <td>Service Tax: $5.00</td>
              <td>Rounded $: ${rounded$}</td>
            </tr>
          </tbody>
        </table>
        <div className="final-amount">
          <strong>Final Total: $115.00</strong>
        </div>
      </div>
      <div className="speaker-section">
        <img src={speakerGif} alt="Speaker" className="speaker-gif" />
      </div>
    </div>
  );
}

export default CurrentOrder;
