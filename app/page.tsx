"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import landingImg from "@/assets/landing.png";
import { projectByLinks } from "@/constants/projectByLinks";
import { socialLinks } from "@/constants/socialLinks";
import Image from "next/image";

export default function Home() {
    const [isDarkMode, setIsDarkMode] = useState<boolean>(false);

    useEffect(() => {
        const savedDarkMode = localStorage.getItem("darkmode") === "true";
        setIsDarkMode(savedDarkMode);

        document.body.classList.toggle("dark", savedDarkMode);
    }, []);

    const toggleDarkMode = () => {
        const newDarkMode = !isDarkMode;
        setIsDarkMode(newDarkMode);

        document.body.classList.toggle("dark", newDarkMode);
        localStorage.setItem("darkmode", String(newDarkMode));
    };

    return (
        <>
            <nav className="fixed inset-x-0 top-0 z-40 border-b bg-white py-6 dark:border-zinc-500 dark:bg-zinc-900">
                <div className="container flex items-center justify-between">
                    <Link
                        className="bg-gradient-to-br from-indigo-600 to-rose-400 bg-clip-text font-bold text-transparent"
                        href="/"
                    >
                        OpenSeries
                    </Link>
                    <div className="flex items-center gap-6">
                        <Link
                            className="font-medium text-zinc-500 transition-all duration-300 hover:text-indigo-600 dark:text-zinc-400"
                            href="/docs"
                        >
                            Docs
                        </Link>
                        <div className="flex items-center gap-2">
                            {socialLinks.map((link) => (
                                <Link
                                    key={link.name}
                                    href={link.href}
                                    target="_blank"
                                    className={`${link.icon} text-xl text-zinc-500 transition-all  duration-300 hover:text-indigo-600 dark:text-zinc-400`}
                                ></Link>
                            ))}
                        </div>
                        <div className="flex items-center gap-2">
                            <input
                                className="checked:bg-primary checked:after:bg-primary checked:focus:border-primary checked:focus:bg-primary dark:checked:bg-primary dark:checked:after:bg-primary mr-2 mt-[0.3rem] h-3.5 w-8 appearance-none rounded-[0.4375rem] bg-neutral-300 before:pointer-events-none before:absolute before:h-3.5 before:w-3.5 before:rounded-full before:bg-transparent before:content-[''] after:absolute after:z-[2] after:-mt-[0.1875rem] after:h-5 after:w-5 after:rounded-full after:border-none after:bg-neutral-100 after:shadow-[0_0px_3px_0_rgb(0_0_0_/_7%),_0_2px_2px_0_rgb(0_0_0_/_4%)] after:transition-[background-color_0.2s,transform_0.2s] after:content-[''] checked:after:absolute checked:after:z-[2] checked:after:-mt-[3px] checked:after:ml-[1.0625rem] checked:after:h-5 checked:after:w-5 checked:after:rounded-full checked:after:border-none checked:after:shadow-[0_3px_1px_-2px_rgba(0,0,0,0.2),_0_2px_2px_0_rgba(0,0,0,0.14),_0_1px_5px_0_rgba(0,0,0,0.12)] checked:after:transition-[background-color_0.2s,transform_0.2s] checked:after:content-[''] hover:cursor-pointer focus:outline-none focus:ring-0 focus:before:scale-100 focus:before:opacity-[0.12] focus:before:shadow-[3px_-1px_0px_13px_rgba(0,0,0,0.6)] focus:before:transition-[box-shadow_0.2s,transform_0.2s] focus:after:absolute focus:after:z-[1] focus:after:block focus:after:h-5 focus:after:w-5 focus:after:rounded-full focus:after:content-[''] checked:focus:before:ml-[1.0625rem] checked:focus:before:scale-100 checked:focus:before:shadow-[3px_-1px_0px_13px_#3b71ca] checked:focus:before:transition-[box-shadow_0.2s,transform_0.2s] dark:bg-neutral-600 dark:after:bg-neutral-400 dark:focus:before:shadow-[3px_-1px_0px_13px_rgba(255,255,255,0.4)] dark:checked:focus:before:shadow-[3px_-1px_0px_13px_#3b71ca]"
                                type="checkbox"
                                role="switch"
                                checked={isDarkMode}
                                onChange={toggleDarkMode}
                            />
                        </div>
                    </div>
                </div>
            </nav>
            <main className="flex min-h-dvh items-center justify-center bg-white py-20 dark:bg-zinc-900">
                <div className="container grid items-center gap-10 text-center lg:grid-cols-2 lg:text-left">
                    <div className="order-2 space-y-8 lg:order-1">
                        <h1 className="text-5xl font-black dark:text-zinc-300 sm:text-8xl lg:text-6xl xl:text-7xl 2xl:text-8xl">
                            <span className="bg-gradient-to-br from-indigo-600 to-rose-400 bg-clip-text text-transparent">
                                OpenSeries:{" "}
                            </span>
                            Cheatsheet Matematika & Fisika
                        </h1>
                        <p className="dark:text-zinc-400 sm:text-xl sm:leading-relaxed lg:text-lg xl:text-xl">
                            Solusi Pintar untuk Hitung-Hitung Sekolah! Temukan kemudahan mengatasi segala jenis
                            persamaan dan rumus di bangku SMA/SMK/Sederajat.
                        </p>
                        <div className="flex flex-col items-center gap-6 lg:items-start xl:flex-row xl:items-center">
                            <Link
                                className="whitespace-nowrap rounded-md bg-indigo-600 px-8 py-4 font-medium text-white shadow-2xl shadow-indigo-600/60 transition-all duration-200 hover:bg-indigo-700"
                                href="/docs"
                            >
                                Get Started
                            </Link>
                            <span className="flex flex-wrap items-center gap-2 dark:text-zinc-400">
                                By
                                {projectByLinks.map((link) => (
                                    <Link
                                        key={link.name}
                                        target="_blank"
                                        className="whitespace-nowrap rounded-full border-2 border-rose-400 px-4 py-1 text-xs font-medium text-rose-400 transition-all duration-200 hover:bg-rose-100"
                                        href={link.href}
                                    >
                                        {link.name}
                                    </Link>
                                ))}
                            </span>
                        </div>
                    </div>
                    <Image className="order-1 lg:order-2" src={landingImg} alt="" />
                </div>
            </main>
        </>
    );
}
