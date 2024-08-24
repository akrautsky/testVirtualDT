import React from 'react';
import './Modal.css';
import closeIcon from './close.png'; // Make sure to place the close.png file in the src folder
import Menu from './Menu';
import CurrentOrder from './CurrentOrder';
import { MyOrderProvider } from './myOrderContext';

function Modal({ onClose }) {
  return (
    <MyOrderProvider>
      <div className="modal-overlay">
        <div className="modal-content">
          <img src={closeIcon} className="close-button" alt="Close" onClick={onClose} />
          <div className="modal-body d-flex">
            <div className="menu-section">
              <Menu />
            </div>
            <div className="divider"></div>
            <div className="order-section">
              <CurrentOrder />
            </div>
          </div>
        </div>
      </div>
    </MyOrderProvider>
  );
}

export default Modal;
