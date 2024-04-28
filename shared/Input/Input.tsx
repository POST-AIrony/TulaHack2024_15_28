"use client";
import React, { useState } from "react";

import "./Input.css";

const Input = () => {
  const [response, setResponse] = useState("");
  return (
    <div className="inputBlock">
      <input
        type="text"
        placeholder="Напишите что-то"
        onChange={(event) => setResponse(event.target.value)}
        className="inputBlock_Input"
      />

      <button className="inputBlock_SendButton">
        <svg
          width="50"
          height="45"
          viewBox="0 0 36 30"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M35.4142 16.4142C36.1953 15.6332 36.1953 14.3668 35.4142 13.5858L22.6863 0.857866C21.9052 0.0768175 20.6389 0.0768174 19.8579 0.857866C19.0768 1.63891 19.0768 2.90524 19.8579 3.68629L31.1716 15L19.8579 26.3137C19.0768 27.0948 19.0768 28.3611 19.8579 29.1421C20.6389 29.9232 21.9052 29.9232 22.6863 29.1421L35.4142 16.4142ZM-1.74846e-07 17L34 17L34 13L1.74846e-07 13L-1.74846e-07 17Z"
            fill="black"
          />
        </svg>
      </button>
    </div>
  );
};

export default Input;
