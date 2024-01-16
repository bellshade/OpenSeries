import Link from "next/link";

export default async function Home() {
    return (
        <>
            <nav className="fixed inset-x-0 top-0 py-6">
                <div className="container mx-auto flex items-center justify-between">
                    <Link className="font-bold text-zinc-800" href="/">
                        OpenSeries
                    </Link>
                    <div className="flex items-center gap-6">
                        <Link
                            className="font-medium text-zinc-500 transition-all duration-300 hover:text-zinc-800"
                            href="/docs"
                        >
                            Docs
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
                    </div>
                </div>
            </nav>
            <section className="flex min-h-screen items-center justify-center">
                <div className="container flex flex-col items-center gap-8 text-center">
                    <h1 className="text-balance text-6xl font-black">
                        Selamat datang di <span className="text-zinc-800">OpenSeries</span>
                    </h1>
                    <p className="max-w-2xl text-lg text-zinc-600">
                        Solusi Pintar untuk Hitung-Hitung Sekolah! Temukan kemudahan mengatasi segala jenis persamaan
                        dan rumus di bangku SMA/SMK/Sederajat.
                    </p>
                    <Link
                        className="rounded-md bg-zinc-800 px-6 py-3 font-medium text-white transition-all duration-200 hover:bg-zinc-700"
                        href="/docs"
                    >
                        Get Started
                    </Link>
                    <span className="text-sm font-medium text-zinc-400">
                        By{" "}
                        <Link className="hover:underline" href="">
                            Kelas Terbuka
                        </Link>
                        ,{" "}
                        <Link className="hover:underline" href="">
                            Bellshade
                        </Link>
                        ,{" "}
                        <Link className="hover:underline" href="">
                            WPU
                        </Link>
                    </span>
                </div>
            </section>
        </>
    );
}
