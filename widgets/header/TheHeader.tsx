import React from "react";

import Link from "next/link";

import "./TheHeader.css";

const TheHeader = () => {
  return (
    <header>
      <Link href="/" className="flex items-center">
        <img
          src="/static/EpicLabLogo.svg"
          alt=""
          className="w-[70px] h-[70px]"
        />

        <h2 className="ml-[20px] text-[#ffffff] text-[2.5rem] font-['Montserrat_Alternates'] font-medium">
          EpicLab
        </h2>
      </Link>

      <nav className="flex items-center">
        <Link
          href="/userStories"
          className="bg-gradient-to-r from-[#ffdb5e] to-[#9002ff] inline-block text-transparent bg-clip-text text-[2rem] font-['Montserrat_Alternates'] font-medium"
        >
          Истории пользователей
        </Link>

        <Link
          href="/signIn"
          className="flex justify-center items-center ml-[100px] w-[210px] h-[60px] bg-[#ffffff] rounded-[50px] text-[#000000] text-[2rem] font-[Montserrat_Alternates] font-medium"
        >
          Войти
        </Link>
      </nav>
    </header>
  );
};

export default TheHeader;
