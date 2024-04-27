import React from "react";

import Link from "next/link";

import "./TheMainPageHeader.css";

const TheMainPageHeader = () => {
  return (
    <header>
      <Link href="/" className="flex items-center">
        <img
          src="/static/EpicLabLogo.svg"
          alt=""
          className="logo"
        />

        <h2 className="ml-[20px] text-[#ffffff] text-[2.5rem] font-['Montserrat_Alternates'] font-medium">
          EpicLab
        </h2>
      </Link>

      <nav className="flex items-center">
        <Link
          href="/userStories"
          className="bg-gradient-to-r from-[#ffdb5e] to-[#9002ff] inline-block text-transparent bg-clip-text text-[2rem] font-['Montserrat_Alternates'] font-medium btn_default p"
        >
          Истории пользователей
        </Link>

        <Link
          href="/signIn"
          className="flex justify-center items-center ml-[100px] w-[210px] h-[60px]  font-['Montserrat_Alternates'] font-medium login"
        >
          Войти
        </Link>
      </nav>
    </header>
  );
};

export default TheMainPageHeader;