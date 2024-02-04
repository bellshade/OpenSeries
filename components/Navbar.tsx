"use client";

import { socialLinks } from "@/constants/socialLinks";
import Link from "next/link";
import React, { useState } from "react";
import ThemeSwitcher from "./ThemeSwitcher";
import { navLinks } from "@/constants/navLinks";
import { useNavStyle } from "@/hooks/useNavStyle";

type Props = {};

const Navbar = (props: Props) => {
    const { isLanding } = useNavStyle();
    const [isOpen, setIsOpen] = useState(false);

    const landingStyle = "fixed";
    const docsStyle = "sticky px-8";

    return (
        <nav
            className={`${isLanding ? landingStyle : docsStyle} inset-x-0 top-0 z-40 border-b bg-white/30 py-3 backdrop-blur-lg dark:border-zinc-700 dark:bg-zinc-800/30`}
        >
            <div className={`relative flex items-center justify-between ${isLanding && "container"}`}>
                <Link
                    className="bg-gradient-to-br from-indigo-600 to-rose-400 bg-clip-text font-bold text-transparent"
                    href="/"
                >
                    OpenSeries
                </Link>
                <div className="flex items-center gap-8">
                    <div
                        className={`absolute inset-x-0 top-full mt-3 flex origin-top flex-col gap-x-8 gap-y-6 rounded-lg border bg-white p-12 shadow-2xl dark:border-zinc-700 dark:bg-zinc-800 lg:static lg:m-0 lg:flex-row lg:border-none lg:bg-inherit lg:p-0 lg:shadow-none ${isOpen ? "scale-y-100" : "scale-y-0 lg:scale-y-100"}`}
                    >
                        {navLinks.map((link) => (
                            <Link
                                key={link.name}
                                className="text-lg text-zinc-500 hover:text-indigo-600 dark:text-zinc-400 dark:hover:text-indigo-500 lg:text-sm"
                                href={link.href}
                                target={link.target}
                            >
                                {link.name}
                            </Link>
                        ))}
                    </div>
                    <div className="flex">
                        {socialLinks.map((link) => (
                            <Link
                                key={link.name}
                                href={link.href}
                                target="_blank"
                                className={`grid h-10 w-10  place-items-center rounded-lg text-xl text-zinc-500 hover:bg-zinc-200 dark:text-zinc-400 dark:hover:bg-zinc-700`}
                            >
                                <span className={link.icon}></span>
                            </Link>
                        ))}
                        <ThemeSwitcher />
                        <button
                            onClick={() => setIsOpen(!isOpen)}
                            className={`grid h-10 w-10 place-items-center  rounded-lg text-xl text-zinc-500 hover:bg-zinc-200 dark:text-zinc-400 dark:hover:bg-zinc-700 lg:hidden`}
                        >
                            <span className="icon-[gg--menu]"></span>
                        </button>
                    </div>
                </div>
            </div>
        </nav>
    );
};

export default Navbar;
