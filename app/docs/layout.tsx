import Header from "@/components/Header";
import Sidebar from "@/components/Sidebar";

export default async function MdxLayout({ children }: { children: React.ReactNode }) {
    return (
        <>
            <div className="flex h-screen max-h-screen flex-col overflow-hidden">
                <Header />
                <div className="relative flex h-full pt-[3.6rem]">
                    <Sidebar />
                    <main className="prose h-full w-full max-w-none overflow-y-auto p-6">{children}</main>
                </div>
            </div>
        </>
    );
}
