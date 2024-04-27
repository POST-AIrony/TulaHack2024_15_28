import React from 'react';

import "./TheHeader.css";

const TheHeader = () => {
    return (
        <header>
            <button className="absolute top-[42.5px] left-[50px] w-[40px] h-[40px]">
                <img src="/static/HamburgerMenuIcon.svg" alt="" className="w-full h-full"/>
            </button>

            <h3 className="bg-gradient-to-r from-[#9002ff] to-[#ffdb5e] inline-block text-transparent bg-clip-text text-[4rem] font-['Montserrat_Alternates'] font-extrabold p">EpicLab</h3>
        </header>
    );
};

export default TheHeader;