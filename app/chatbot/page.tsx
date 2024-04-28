"use client";
import React, { useState } from "react";

import TheHeader from "@/widgets/header/TheHeader";

const Page = () => {
  const [response, setResponse] = useState("");

  return (
    <>
      <TheHeader />

      <main className="grid justify-items-center deskWide:px-[calc((100%-1920px)/2)] w-full h-full bg-[#1e1e1e]">
        <section className="relative mb-[50px] w-full h-[calc(100vh-175px)] overflow-y-auto">
          <div className="relative flex flex-col mx-[calc((100%-1325px)/2)] w-[1325px] h-[calc(100%-100px)]">
            <p className="inline-block mt-[30px] py-[40px] px-[40px] max-w-[60%] bg-[#8f02ff] rounded-t-[120px] rounded-br-[120px] text-[#ffffff] text-[2rem] font-['Montserrat'] font-medium">
              Привет, пользователь! Это EpicLab Чат-бот, сделанный специально
              для создания Ваших захватывающих историй.
            </p>

            <p className="inline-block self-end mt-[30px] py-[40px] px-[40px] max-w-[60%] bg-[#ffffff] rounded-t-[120px] rounded-bl-[120px] text-[#000000] text-[2rem] font-['Montserrat'] font-medium">
              Мой персонаж пошел в лес.
            </p>
          </div>

          <div className="relative flex justify-center items-center w-full h-[100px]">
            <input
              type="text"
              placeholder="Напишите что-то"
              onChange={(event) => setResponse(event.target.value)}
              className="px-[50px] w-[1200px] h-full bg-[#1f1f1f] border-[5px] border-[#8f02ff] rounded-l-[50px] placeholder:text-[#ffffff] text-[2rem] font-['Montserrat_Alternates'] font-medium outline-none"
            />

            <button className="flex justify-center items-center w-[125px] h-full bg-gradient-to-tr from-[#ffdb5e] to-[#9002ff] rounded-r-[50px]">
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
        </section>
      </main>
    </>
  );
};

export default Page;
