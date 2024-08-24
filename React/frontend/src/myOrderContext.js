import React, { createContext, useState, useEffect } from 'react';

export const MyOrderContext = createContext();

export const MyOrderProvider = ({ children }) => {
  const [myOrder, setMyOrder] = useState([]);
  

//   useEffect(() => {
//     console.log('myOrder updated:', myOrder);
//   }, [myOrder]);

  return (
    <MyOrderContext.Provider value={{ myOrder, setMyOrder }}>
      {children}
    </MyOrderContext.Provider>
  );
};
