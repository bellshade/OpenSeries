import Link from "next/link";
import React from "react";

type Props = {};

export default function Header({}: Props) {
    return (
        <header className="fixed inset-x-0 top-0 z-10 flex items-center justify-between border-b bg-white px-6 py-4">
            <Link className="font-bold text-zinc-800" href="/">
                OpenSeries
            </Link>
            <div className="flex items-center gap-2">
                <Link
                    href="/github"
                    className="icon-[mdi--github] text-xl text-zinc-500 transition-all duration-300 hover:text-zinc-800"
                ></Link>
                <Link
                    href="/github"
                    className="icon-[ic--baseline-discord] text-xl text-zinc-500 transition-all duration-300 hover:text-zinc-800"
                ></Link>
            </div>
        </header>
    );
}
