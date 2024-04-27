"use client";
import React, { useState } from "react";

import Link from "next/link";

import TheHamburgerMenu from "@/widgets/hamburgerMenu/TheHamburgerMenu";

import "./TheHeader.css";

const TheHeader = () => {
  const [isOpened, changeIsOpenedStatus] = useState(false);

  return (
    <>
      <header>
        <button
          onClick={() => changeIsOpenedStatus(true)}
          className="absolute top-[42.5px] left-[50px] w-[40px] h-[40px]"
        >
          <img
            src="/static/HamburgerMenuIcon.svg"
            alt=""
            className="w-full h-full"
          />
        </button>

        <Link
          href="/"
          className="bg-gradient-to-r from-[#9002ff] to-[#ffdb5e] inline-block text-transparent bg-clip-text text-[4rem] font-['Montserrat_Alternates'] font-extrabold p outline-none"
        >
          EpicLab
        </Link>
      </header>

      <TheHamburgerMenu
        isOpened={isOpened}
        handleHamburgerMenuClose={() => changeIsOpenedStatus(false)}
      />
    </>
  );
};

export default TheHeader;
