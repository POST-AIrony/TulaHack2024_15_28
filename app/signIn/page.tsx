import Link from "next/link";

import { teamList } from "@/data/team";

export default function Home() {
  return (
    <>
      <main className="w-full h-auto">
        <div className=" w-full h-[1080px] bg-[url('/static/purple.svg')] block-image">
          <h1 className="bg-gradient-to-r from-[#9002ff] to-[#ffdb5e] inline-block text-transparent bg-clip-text text-[8rem] font-['Montserrat_Alternates'] font-extrabold p-center">
            EpicLab
          </h1>
          <div className="bubble">
          <h1 className="inline-block text-transparent bg-clip-text text-[8rem] font-['Montserrat_Alternates'] font-extrabold log">Вход</h1>
          <input type="text" placeholder="Имя пользователя" className="font-['Montserrat_Alternates'] font-extrabold input"/><br/>
          <input type="password" placeholder="Пароль" className="font-['Montserrat_Alternates'] font-extrabold input"/>
          
          
        <Link
          href="/signIn"
          className="flex justify-center items-center ml-[100px] w-[210px] h-[60px]  font-['Montserrat_Alternates'] font-medium login button"
        >
          Войти
        </Link>
        <h1 className="font-[Montserrat_Alternates] font-extrabold predlog">Еще нет аккаунта? </h1>
        <Link
          href="/signIn"
          className="font-[Montserrat_Alternates] font-extrabold otvet"
        >
          Зарегистрируйтесь!
        </Link>
        </div>
        </div>
      </main>
    </>
  );
}
