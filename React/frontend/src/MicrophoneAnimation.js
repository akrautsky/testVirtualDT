import React from 'react';
import './MicrophoneAnimation.css';

function MicrophoneAnimation({ listening }) {
  return (
    <div className={`microphone ${listening ? 'listening' : ''}`}>
      <div className="mic-circle"></div>
      <div className="sound-wave"></div>
    </div>
  );
}

export default MicrophoneAnimation;
