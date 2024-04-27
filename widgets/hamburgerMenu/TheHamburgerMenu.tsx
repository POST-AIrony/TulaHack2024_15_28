"use client";
import React from "react";

import Link from "next/link";

import "./TheHamburgerMenu.css";

const TheHamburgerMenu: React.FC<{
  isOpened: boolean;
  handleHamburgerMenuClose: () => void;
}> = ({ isOpened, handleHamburgerMenuClose }) => {
  return (
    <>
      <aside
        className={`fixed top-0 py-[30px] px-[40px] w-[500px] h-screen bg-[#1b1b1b] duration-[500ms] ease-in-out z-30 ${isOpened ? "left-0" : "left-[-500px]"}`}
      >
        <button
          onClick={() => handleHamburgerMenuClose()}
          className="flex justify-center items-center w-[65px] h-[65px]"
        >
          <img src="/static/XMarkIcon.svg" alt="" className="w-full h-full" />
        </button>

        <nav className="mt-[125px]">
          <Link href="/userStories" className="flex items-center outline-none">
            <img
              src="/static/UserStoriesIcon.svg"
              alt=""
              className="w-[55px] h-[55px]"
            />

            <p className="ml-[40px] text-[#ffffff] text-[2rem] font-['Montserrat'] font-medium">
              Истории других пользователей
            </p>
          </Link>

          <Link
            href="/chatbot"
            className="flex items-center outline-none mt-[50px]"
          >
            <img
              src="/static/ChatbotIcon.svg"
              alt=""
              className="w-[55px] h-[55px]"
            />

            <p className="ml-[40px] text-[#ffffff] text-[2rem] font-['Montserrat'] font-medium">
              Чат-бот
            </p>
          </Link>

          <button className="absolute bottom-[30px] flex items-center outline-none mt-[50px]">
            <img
              src="/static/SignOutIcon.svg"
              alt=""
              className="w-[55px] h-[55px]"
            />

            <p className="ml-[40px] text-[#ffffff] text-[2rem] font-['Montserrat'] font-medium">
              Выйти из аккаунта
            </p>
          </button>
        </nav>
      </aside>

      <div className="fixed w-full h-full bg-[#1e1e1e] opacity-75 z-20"></div>
    </>
  );
};

export default TheHamburgerMenu;
