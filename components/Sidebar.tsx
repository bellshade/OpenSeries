"use client";

import { documentations } from "@/constants/documentations";
import { socialLinks } from "@/constants/socialLinks";
import Link from "next/link";
import { usePathname } from "next/navigation";
import React, { Fragment, useState } from "react";
type Props = {};

export default function Sidebar({}: Props) {
    const pathname = usePathname();
    const [isOpen, setIsOpen] = useState(false);

    return (
        <>
            <aside
                className={`absolute inset-y-0 z-20 flex min-w-[300px] max-w-[300px]  grow flex-col gap-4 overflow-y-auto border-r bg-white p-10 transition-all duration-300 md:static md:translate-x-0 ${isOpen ? "translate-x-0" : "-translate-x-[calc(100%+0.6rem)]"}`}
            >
                <header className="flex items-center justify-between border-b pb-3">
                    <Link
                        className="bg-gradient-to-br from-indigo-600 to-rose-400 bg-clip-text font-bold text-transparent"
                        href="/"
                    >
                        OpenSeries
                    </Link>
                    <div className="flex items-center gap-2">
                        {socialLinks.map((link) => (
                            <Link
                                key={link.name}
                                href={link.href}
                                target="_blank"
                                className={`${link.icon} text-xl text-zinc-500 transition-all duration-300 hover:text-indigo-600`}
                            ></Link>
                        ))}
                    </div>
                </header>
                {documentations.map((documentation) => (
                    <Fragment key={documentation.parent}>
                        <span className="text-xs font-bold uppercase text-zinc-800">{documentation.parent}</span>
                        <div className="flex flex-col">
                            {documentation.childs.map((link) => (
                                <Link
                                    key={link.href}
                                    className={`border-l-2 py-2 pl-6 text-sm transition-all duration-200 hover:border-l-indigo-600 hover:text-indigo-600 ${link.href === pathname ? "border-l-indigo-600 text-indigo-600" : "text-zinc-400"}`}
                                    href={link.href}
                                    onClick={() => setIsOpen(false)}
                                >
                                    {link.title}
                                </Link>
                            ))}
                        </div>
                    </Fragment>
                ))}
            </aside>
            <button
                onClick={() => setIsOpen(!isOpen)}
                className={`absolute bottom-5 right-5 flex items-center gap-1 rounded-full bg-zinc-800 px-2 py-2 text-white sm:px-6 md:hidden`}
            >
                <span className="hidden sm:block">{isOpen ? "Close" : "Open"} Menu</span>
                {isOpen ? (
                    <span className="icon-[ph--x] text-xl"></span>
                ) : (
                    <span className="icon-[ic--round-menu] text-xl"></span>
                )}
            </button>
        </>
    );
}
