"use client";
import React, {useState} from 'react';

import TheHeader from "@/widgets/header/TheHeader";

const Page = () => {
    const [inviteLink, setInviteLink] = useState("");

    return (
        <>
         <TheHeader/>

          <main className="grid justify-items-center deskWide:px-[calc((100%-1920px)/2)] w-full h-full bg-[#1e1e1e]">
              <h1 className="bg-gradient-to-r from-[#9002ff] to-[#ffdb5e] inline-block text-transparent bg-clip-text text-[6rem] font-['Montserrat_Alternates'] font-medium p">
                  Истории пользователей
              </h1>

              <div className="relative flex items-center mt-[50px] w-[1325px] h-[100px]">
                  <input type="text" placeholder="Вставьте ссылку-приглашение" onChange={(event) => setInviteLink(event.target.value)} className="px-[50px] w-[1200px] h-full bg-[#1f1f1f] border-[5px] border-[#8f02ff] rounded-l-[50px] placeholder:text-[#ffffff] text-[2rem] font-['Montserrat_Alternates'] font-medium"/>

                  <button className="flex justify-center items-center w-[125px] h-full bg-gradient-to-tr from-[#ffdb5e] to-[#9002ff] rounded-r-[50px]">
                      <svg width="50" height="45" viewBox="0 0 36 30" fill="none" xmlns="http://www.w3.org/2000/svg">
                          <path d="M35.4142 16.4142C36.1953 15.6332 36.1953 14.3668 35.4142 13.5858L22.6863 0.857866C21.9052 0.0768175 20.6389 0.0768174 19.8579 0.857866C19.0768 1.63891 19.0768 2.90524 19.8579 3.68629L31.1716 15L19.8579 26.3137C19.0768 27.0948 19.0768 28.3611 19.8579 29.1421C20.6389 29.9232 21.9052 29.9232 22.6863 29.1421L35.4142 16.4142ZM-1.74846e-07 17L34 17L34 13L1.74846e-07 13L-1.74846e-07 17Z" fill="black"/>
                      </svg>
                  </button>
              </div>

              <section className="relative mt-[100px] w-full h-auto">
                    {/*<div className="relative p-[30px] w-[400px] h-[400px] bg-[#8f02ff] rounded-[50px] overflow-hidden">*/}
                    {/*    <p className="w-full h-full text-[#ffffff] text-[2.25rem] line-clamp-6 font-['Montserrat'] font-bold">Вы находитесь в кафе под названием "Allelleo". Это небольшое, уютное заведение с атмосферой</p>*/}
                    {/*</div>*/}
              </section>
          </main>
        </>
    );
};

export default Page;